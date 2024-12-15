from django.db import models

import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)

class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(('The username must be set'))
        username = self.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser):

    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, blank=True, null=True)
    age = models.IntegerField(default=None, null=True)
    sex = models.CharField(max_length=10, default=None, null=True)
    main_goal = models.CharField(max_length=100, default=None, null=True)
    description = models.TextField(default=None, null=True)
    inst = models.CharField(max_length=100, default=None, null=True)
    telegram = models.CharField(max_length=100, default=None, null=True)
    x_network = models.CharField(max_length=100, default=None, null=True)
    hobby = models.CharField(max_length=100, default=None, null=True)
    username = models.CharField(max_length=100, unique=True, default=None, null=False)
    password = models.CharField(default=None, max_length=255, null=False)
    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now())
    photo1 = models.ImageField(upload_to='images/', default=None, null=True)
    photo2 = models.ImageField(upload_to='images/', default=None, null=True)
    photo3 = models.ImageField(upload_to='images/', default=None, null=True)
    photo4 = models.ImageField(upload_to='images/', default=None, null=True)
    photo5 = models.ImageField(upload_to='images/', default=None, null=True)
    photo6 = models.ImageField(upload_to='images/', default=None, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return f"'id': {self.id}, 'first_name': '{self.first_name}', 'last_name': '{self.last_name}', 'username': '{self.username}', 'created_at': {int(self.created_at.timestamp())}, 'updated_at': {int(self.updated_at.timestamp())}, 'role': {self.role}, 'is_active': {self.is_active}"

    def __repr__(self):
        return f"{CustomUser.__name__}(id={self.id})"

    @staticmethod
    def get_by_id(user_id):
        custom_user = CustomUser.objects.filter(id=user_id).first()
        return custom_user if custom_user else None

    @staticmethod
    def get_by_username(username):
        custom_user = CustomUser.objects.filter(username=username).first()
        return custom_user if custom_user else None

    @staticmethod
    def delete_by_id(user_id):
        user_to_delete = CustomUser.objects.filter(id=user_id).first()
        if user_to_delete:
            CustomUser.objects.filter(id=user_id).delete()
            return True
        return False

    @staticmethod
    def create(username, password, first_name=None, middle_name=None, last_name=None):
        if len(first_name) <= 20 and len(middle_name) <= 20 and len(last_name) <= 20 and len(username) <= 100 and len(
                username.split('@')) == 2 and len(CustomUser.objects.filter(username=username)) == 0:
            custom_user = CustomUser(username=username, password=password, first_name=first_name, middle_name=middle_name,
                                     last_name=last_name)
            custom_user.save()
            return custom_user
        return None

    def to_dict(self):
        return {'id': self.id,
                'first_name': f'{self.first_name}',
                'last_name': f'{self.last_name}',
                'username': f'{self.username}',
                'created_at': int(self.created_at.timestamp()),
                'updated_at': int(self.updated_at.timestamp()),
                'role': self.role,
                'is_active': self.is_active}

    def update(self,
               first_name=None,
               last_name=None,
               middle_name=None,
               password=None,
               role=None,
               is_active=None):
        
        user_to_update = CustomUser.objects.filter(username=self.username).first()
        if first_name != None and len(first_name) <= 20:
            user_to_update.first_name = first_name
        if last_name != None and len(last_name) <= 20:
            user_to_update.last_name = last_name
        if middle_name != None and len(middle_name) <= 20:
            user_to_update.middle_name = middle_name
        if password != None:
            user_to_update.password = password
        if role != None:
            user_to_update.role = role
        if is_active != None:
            user_to_update.is_active = is_active
        user_to_update.save()

    @staticmethod
    def get_all():
        return CustomUser.objects.all()

    def get_role_name(self):
        return ROLE_CHOICES[self.role][1]

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        return False
    
    def has_perm(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        return False