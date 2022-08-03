from multiprocessing import Condition
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.deletion import SET_NULL
from authentication.models import User


class Customer(models.Model):
    firstName = models.CharField(max_length=15, null=True, blank=True)
    lastName = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)