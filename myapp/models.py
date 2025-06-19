from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class TeacherManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("Teachers must have an email address")
#         teacher = self.model(email=self.normalize_email(email))
#         teacher.set_password(password)
#         teacher.save(using=self._db)
#         return teacher

#     def create_superuser(self, email, password=None):
#         teacher = self.create_user(email, password)
#         teacher.is_admin = True
#         teacher.save(using=self._db)
#         return teacher

# class Teacher(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = TeacherManager()

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

class FA1(models.Model):
    no = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    name = models.CharField(max_length=100)
    eng = models.DecimalField(max_digits=5, decimal_places=2)
    kan = models.IntegerField()
    hin = models.IntegerField()
    maths = models.IntegerField()
    sci = models.IntegerField()
    soc_sci = models.IntegerField()

    @property
    def total(self):
        return self.eng + self.kan + self.hin + self.maths + self.sci + self.soc_sci

    def __str__(self):
        return self.name
    
class FA2(models.Model):
    no = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    name = models.CharField(max_length=100)
    eng = models.DecimalField(max_digits=5, decimal_places=2)
    kan = models.IntegerField()
    hin = models.IntegerField()
    maths = models.IntegerField()
    sci = models.IntegerField()
    soc_sci = models.IntegerField()

    @property
    def total(self):
        return self.eng + self.kan + self.hin + self.maths + self.sci + self.soc_sci

    def __str__(self):
        return self.name


class FA3(models.Model):
    no = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    name = models.CharField(max_length=100)
    eng = models.DecimalField(max_digits=5, decimal_places=2)
    kan = models.IntegerField()
    hin = models.IntegerField()
    maths = models.IntegerField()
    sci = models.IntegerField()
    soc_sci = models.IntegerField()

    @property
    def total(self):
        return self.eng + self.kan + self.hin + self.maths + self.sci + self.soc_sci

    def __str__(self):
        return self.name



class FA4(models.Model):
    no = models.AutoField(primary_key=True)
    slno = models.IntegerField()
    name = models.CharField(max_length=100)
    eng = models.DecimalField(max_digits=5, decimal_places=2)   
    kan = models.IntegerField()
    hin = models.IntegerField()
    maths = models.IntegerField()
    sci = models.IntegerField()
    soc_sci = models.IntegerField()

    @property
    def total(self):
        return self.eng + self.kan + self.hin + self.maths + self.sci + self.soc_sci

    def __str__(self):
        return self.name