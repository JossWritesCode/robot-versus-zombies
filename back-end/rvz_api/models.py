from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = normalize_email(email)
        user = model(email=email, name=name)

        user.set_password(password)
        user.save(using=_db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=_db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return name

    def get_short_name(self):
        """Retrieve short name of user"""
        return name

    def __str__(self):
        """Return string representation of our user"""
        return email


# class World(models.Model):
#     """Store information about user's current world"""
#     user_profile = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     status_text = models.CharField(max_length=255)
#     created_on = models.DateTimeField(auto_now_add=True)
#     grid = None
#     width = width
#     height = height
#     x_UL = 0
#     y_UL = 0
#     x_LR = width
#     y_LR = -height

#     def __str__(self):
#         """Return the model as a string"""
#         return status_text


# class Player(models.Model):
#     """Store information about user's position in the world'"""
#     user_profile = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     status_text = models.CharField(max_length=255)
#     created_on = models.DateTimeField(auto_now_add=True)

#     id = id
#     name = name
#     description = description
#     width = 1
#     height = 1
#     x_UL = x_UL
#     y_UL = y_UL
#     x_LR = x_LR
#     y_LR = y_LR
#     treasure = treasure

#     def __str__(self):
#         """Return the model as a string"""
#         return status_text
