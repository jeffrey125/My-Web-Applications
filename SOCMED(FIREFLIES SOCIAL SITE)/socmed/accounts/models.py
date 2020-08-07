from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        # username comes from the auth.models.User
        return '@{}'.format(self.username)
