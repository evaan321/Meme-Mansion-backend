from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank = True)
    firstName = models.CharField(max_length=20, blank = True)
    lastName = models.CharField(max_length=20, blank = True)
    bio   = models.CharField(max_length = 50, blank = True)
    avater = models.ImageField(upload_to='avater/' , blank= True)
    