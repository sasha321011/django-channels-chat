from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create(self,email,password=None,**extra_field):
        if not email:
            raise ValueError('USER MUST NEED EMAIL')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_field)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_super(self,email,password=None,**extra_field):
        extra_field.setdefault("is_staff",True)
        extra_field.setdefault("is_superuser", True)
        return self.create_user(email,password=password,**extra_field)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_join = models.DateTimeField(auto_now_add=True)

    object = UserManager()

    USERNAMEFIELD = 'email'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
