from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, lastname, firstname, birthday, sex, password=None):
        if not email:
            raise ValueError('Email를 입력해주세요')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            lastname = lastname,
            firstname = firstname,
            birthday = birthday,
            sex = sex,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, lastname, firstname, birthday, sex, password):
        u = self.create_superuser(email = email,
                                  lastname=lastname,
                                  firstname=firstname,
                                  birthday=birthday,
                                  sex=sex,
                                  )
        u.is_admin = True
        u.save(using=self._db)
        return u

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = 'email',
        max_length = 255,
        unique = True,
    )
    lastname = models.CharField(
        u'이름',
        max_length = 10,
        blank = False,
        unique = True,
        default = ''
    )
    firstname = models.CharField(
        u'성',
        max_length=10,
        blank=False,
        unique=True,
        default=''
    )
    sex = models.CharField(
        u'성별',
        max_length=5,
        blank=False,
        unique=True,
        default=''
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

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
        # Simplest possible answer: All admins are staff
        return self.is_admin