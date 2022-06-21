from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


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


class Orders(models.Model):
    user_id = models.ManyToManyField(User, on_delete=models.CASCADE, primary_key=True) # &&
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNumberRegex = RegexValidator(regex=r"^\+375\d{9}$") # я не знаю можно ли так в классе прописывать функцию или ее вообще вынести в отдельный файл
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    photo = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.title


