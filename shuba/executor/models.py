from django.contrib.auth.models import User
from django.db import models



class Speciality(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'speciality'

    def __str__(self):
        return self.title


class Executor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12) # ???????
    city = models.CharField(max_length=50)
    photo = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField(default=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    speciality = models.ManyToManyField(Speciality)

    class Meta:
        db_table = 'executor'

    def __str__(self):
        return self.last_name




