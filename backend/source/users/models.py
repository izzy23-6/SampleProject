from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.conf import settings
from source.CDR import SpanningForeignKey
import uuid
import datetime
from django.utils import timezone


def jwt_get_secret_key(user_model):
    """ Secret key generator for JSON Web Token for extra security  """
    return user_model.jwt_secret

class UserManager(BaseUserManager):
    """ Custom User model table manager """
    def create_user(self, username, email, full_name, is_active=True, is_staff=False, is_admin=False, password=None):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email')
        if not full_name:
            raise ValueError("User must have a full name")
        user = self.model(
            username = username, 
            email = self.normalize_email(email),
            full_name = full_name,
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, username, email, full_name, password=None):
        user = self.create_user(
            username,
            email,
            full_name,
            is_staff=True,
            is_admin=True,
            password=password,
        )
        return user

    def create_superuser(self, username, email, full_name, password=None):
        user = self.create_user(
            username,
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True,
            # is_superuser=True
        ),
        # user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

    

class User(AbstractBaseUser):
    """ Custom User model contoller for the User table """
    username            = models.CharField(max_length=255, unique=True)
    email               = models.EmailField(max_length=255, unique=True)
    full_name           = models.CharField(max_length=255, blank=True, null=True)
    custparent          = models.ManyToManyField('portal.Custparent', related_name='facility', through='Relation')
    active              = models.BooleanField(default=True)
    staff               = models.BooleanField(default=False)
    admin               = models.BooleanField(default=False)
    jwt_secret          = models.UUIDField(default=uuid.uuid4)
    created_at          = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name' ]

    objects = UserManager()

    class Meta:
        db_table = 'user'


    def facility(self):
        """ Allows the facility field to be seen in the admin """
        return ", ".join([str(c) for c in self.custparent.all()])
        

    def has_perm(self, perm, obj=None):
        """ Custom permissions """
        return True

    
    def has_module_perms(self, app_label):
        """ Custom permissions """
        return True

    @property
    def is_active(self):
        return self.active
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    


class Relation(models.Model):
    """ Many to Many Relationship table for the Users and the Custparent table """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    custparent = SpanningForeignKey('portal.Custparent', related_name='profile', on_delete=models.DO_NOTHING)

    class Meta:
        db_table= 'relation'
        unique_together = ('user', 'custparent')

