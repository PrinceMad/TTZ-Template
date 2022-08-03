from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User, role_master, company_master
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import threading
from rest_framework.response import Response
from .jwtToken import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, JWTAuthentication
import datetime, random, string
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from .models import User, role_master, company_master, UserToken, Reset
from .serializers import UserSerializer, role_masterSerializer, company_masterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from django.http import JsonResponse


class User_viewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class LastUserViewSet(APIView):
    def get(self,request):
        queryset = User.objects.last()
        serializer = UserSerializer(queryset)

        return Response(serializer.data)

class role_master_viewsets(viewsets.ModelViewSet):
    queryset = role_master.objects.all()
    serializer_class = role_masterSerializer
    permission_classes = [IsAuthenticated]

class company_master_viewsets(viewsets.ModelViewSet):
    queryset = company_master.objects.all()
    serializer_class = company_masterSerializer
    # permission_classes = [IsAuthenticated]



class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise APIException('Passwords do not match!')

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()


        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        utoken = UserToken.objects.create(
            user_id = user.id,
            token = refresh_token,
            expired_at = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        )


        response = Response()
        # response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)

        response.data = {
            'token': access_token,
            'r_token': refresh_token,

            'email': user.email,
            'role':str(user.role),
            'position': user.position,
            'name': user.first_name,
            'id': user.id

        }

        return response


    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        utoken = UserToken.objects.create(
            user_id = user.id,
            token = refresh_token,
            expired_at = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        )
       

        response = Response()
        # response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        
        response.data = {
            'token': access_token,
            'r_token': refresh_token,
            
            'email': user.email,
            'role':str(user.role),
            'position': user.position,
            'name': user.first_name,
            'id': user.id
        }

        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        refresh_token = request.data['r_token']
        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
            user_id = id,
            token = refresh_token,
            expired_at__gt = datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists:
            raise AuthenticationFailed('unauthenticated')

        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        # refresh_token = request.COOKIES.get('refreshToken')
        refresh_token = request.data['r_token']
        ut = UserToken.objects.filter(token = refresh_token)
        ut.delete()
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response


class forgotAPIView(APIView):
    def post(self, request):
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        email = request.data['email']
        Reset.objects.create(
            email = email,
            token = token
        )
        
        url = 'http://localhost:8080/reset/' + token

        send_mail(
            'Reset your password!',
            'Click <a href="%s">here</a> to reset your password!' % url,
            settings.EMAIL_FROM_USER,
            [email],
            fail_silently=False,
        )

        return Response({
            'message': 'success'
        })


class ResetAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise APIException('Passwords do not match!')


        reset = Reset.objects.filter(token=data['token']).first()

        if not reset:
            raise APIException('Invalid link!')
        
        user = User.objects.filter(email=reset.email).first()

        if not user:
            raise APIException('User not found!')


        user.set_password(data['password'])
        user.save()

        return Response({
            'message': 'success'
        })

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

# Pacel Registered
@api_view(['GET', 'POST'])
def parcel_arrived_email(request):
    emailadd = ''
    name = ''
    description = ''
    value = ''
    hawb = ''
    weight = ''
    tracking = ''

    if request.data:
        name = request.data['contactName']
        emailadd = request.data['contactEmail']
        description = request.data['description']
        value = request.data['value']
        hawb = request.data['hawb']
        weight = request.data['weight']
        cusId = request.data['cusId']
        tracking = request.data['tracking']

    domain = get_current_site(request)
    current_site = str(domain) + '/notifications'
    email_subject = 'Parcel Arrived At UK Warehouse'
    email_body = render_to_string('emailLocation1.html', {
                    'name': name,
                    'description': description,
                    'value':value,
                    'hawb':hawb,
                    'current_site' : current_site,
                    'cusId': cusId,
                    'weight': weight,
                    'tracking': tracking
                    })
    # if emailadd or name or sender:
    # return JsonResponse({"success": False})
    # else:
    # return JsonResponse({"success": True})

    email = EmailMessage(subject=email_subject, body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=[emailadd]
        )
    email.content_subtype = "html"
    if email:
        print(" == I am message",name,emailadd)

    if not settings.TESTING:
        EmailThread(email).start()

    if email:
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})