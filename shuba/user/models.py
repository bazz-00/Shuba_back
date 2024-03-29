import jwt
import os
import re
import base64
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .tasks import send_register_email_task

from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user( email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def register_token(self):
        return base64.b64encode(self.email.encode()).decode()

    @classmethod
    def activate(cls, register_token):
        email = base64.b64decode(register_token).decode()
        print("Username", email)
        user = cls.objects.filter(email=email).first()
        if user:
            print("USER", user)
            user.is_active = True
            user.save()
        return user

    def send_register_mail(self):
        # send_register_email_task.delay({
        #     "username": self.username,
        #     "register_token": self.register_token
        # })
        send_register_email_task.delay(self.id)

    def __str__(self):
        return self.email

