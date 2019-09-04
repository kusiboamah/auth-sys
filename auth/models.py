from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as gs

# Create your models here.
class User(AbstractBaseUser):
    """User Model. """
    
    username = None
    email = models.EmailField(gs('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []