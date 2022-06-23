from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex=r"^\+375\d{9}$")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    #photo = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.title
