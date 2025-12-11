from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# -------------------------------------------------------------
# Custom User Manager
# -------------------------------------------------------------
class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, role=None):
        if not username:
            raise ValueError("Users must have a username")
        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
            username=username,
            phone_number=phone_number,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password):
        user = self.create_user(
            username=username,
            phone_number=phone_number,
            password=password,
            role=None
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# -------------------------------------------------------------
# Role Model
# -------------------------------------------------------------
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# -------------------------------------------------------------
# Custom User Model
# -------------------------------------------------------------
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
