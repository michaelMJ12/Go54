from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin




class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254, blank=True)
    image = models.ImageField(upload_to='media' , blank=True)
    phone = models.CharField(max_length=225, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)
    date_joined = models.DateTimeField(auto_now=True , blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip() or self.email

    def get_short_name(self):
        return self.email
    




class StudentRecord(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)
    gender = models.CharField(max_length=225, blank=True,null=True)
    month = models.CharField(max_length=10, blank=True,null=True)
    email = models.CharField(max_length=255, blank=True,null=True)
    course = models.CharField(max_length=225, blank=True,null=True)
    phone_number = models.CharField(max_length=225, blank=True,null=True)
    address = models.CharField(max_length=255, blank=True,null=True)
    current_program = models.CharField(max_length=500, blank=True,null=True)
    academic_performance = models.CharField(max_length=500, blank=True,null=True)
    area_of_specializations = models.CharField(max_length=500, blank=True,null=True)
    leadership_positions_held = models.CharField(max_length=200, blank=True,null=True)
    duration_of_leadership_roles = models.CharField(max_length=255, blank=True,null=True)
    leadership_achievements_and_responsibilities = models.CharField(max_length=255, blank=True,null=True)
    year_of_study = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    value = models.CharField(max_length=225, blank=True, null=True)
    state = models.CharField(max_length=225, blank=True,null=True)
    country = models.CharField(max_length=225,blank=True,null=True)
    resume_cv_upload = models.FileField(upload_to='media',null=True)
    file_uploads = models.FileField(upload_to='media',null=True)
    image = models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return self.first_name
    
    



class Ceo(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name
    
    
    
class Message(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)
    email = models.EmailField(unique=True , max_length=225, blank=True,null=True)
    subject = models.CharField(max_length=225, blank=True,null=True)
    message = models.TextField(max_length=1000, blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
     
     
class About(models.Model):
    description = models.TextField(max_length=1000, blank=True , null=True)
    
   
    
    


class Course(models.Model):
    course_name = models.CharField(max_length=225, blank=True)
    course_price = models.CharField(max_length=225, blank=True)
    course_description = models.TextField(max_length=1000, blank=True)
    duration = models.CharField(max_length=225, blank=True)
    start_date = models.DateField(blank=True, default=None, null=True)    
    
    def __str__(self):
        return self.course_name