from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Helps django work with out custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) #encrypts the pw for us
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a 'user profile' inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # a requirement for adding a custom user model to django
    # can be used to disable user accounts
    is_staff = models.BooleanField(default=False)
    # also required for custome user model [?]

    objects = UserProfileManager()
    # to manage user accounts
    # required when subbing, can create admin user, regular user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # can require as many fields as you like

    def get_full_name(self):
        """Used to get a user's full name."""

        return self.name

    def get_short_name(self):
        """Used to get a user's short name."""

        return self.name

    def __str__(self):
        return self.email
