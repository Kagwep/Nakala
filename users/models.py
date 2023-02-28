from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self,email,username, first_name,last_name,phone_number,password=None):
        if not email:
            raise ValueError('please enter a valid email')
        if not username:
            raise ValueError('please enter a username')
        if not first_name:
            raise ValueError('please enter your first name')
        if not last_name:
            raise ValueError('please enter your last name')
        
        if not phone_number:
            raise ValueError('please enter a phone number')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username, first_name,last_name,phone_number,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            password = password
            
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

#custom user
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email',unique=True)
    username = models.CharField(max_length=200, verbose_name= 'username',unique=True)
    first_name = models.CharField(max_length=200,verbose_name= 'first name',null=True)
    last_name =    models.CharField(max_length=200,verbose_name= 'last name',null=True)
    phone_number = models.CharField(max_length=200, verbose_name= 'phone number',null=True,unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone_number','first_name','last_name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

   


