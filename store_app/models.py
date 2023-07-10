from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    iin = models.CharField(max_length=12, validators=[MinLengthValidator(12)])

# OneToMany/ManyToOne -> ForeignKey
# ManyToMany
# OneToOne
