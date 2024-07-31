from djongo import models
import uuid
from django_enumfield import enum

# Create your models here.
from email.policy import default
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



# Create your models here.
#* MODEL FOR OUR ADMIN
class AdminsManager(BaseUserManager):
    def create_user(self, Email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not Email:
            raise ValueError('Users must have an email address')

        user = self.model(
            Email=self.normalize_email(Email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, Email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            Email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            Email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user




class Admin(AbstractBaseUser):
    class STATUS_user(enum.Enum):
        ACTIVE = 1
        UNACTIVE = 2
        DISABLED = 3

    id = models.BigAutoField(primary_key=True,editable=False)
    Email = models.CharField(max_length=254,unique=True)
    # Password = models.CharField(default='',max_length=254,blank=True)
    Ver_code = models.CharField(default='',max_length=254,blank=True)
    Create_datetime = models.DateTimeField(auto_now_add=True)
    Status = enum.EnumField(STATUS_user, default=2)    #2:unactive 1:active  3:disabled
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'Email'

    objects = AdminsManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.Email

    def get_short_name(self):
        # The user is identified by their email address
        return self.Email

    def __str__(self):
        return self.Email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin



# Create your models here.
