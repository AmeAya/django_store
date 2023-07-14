from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    iin = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    photo = models.ImageField(upload_to='customers/', null=True, blank=True)


class Good(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()  # Если null и blank не указаны. Значит они False
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='goods/', null=True, blank=True)


# OneToMany/ManyToOne -> ForeignKey
# ManyToMany
# OneToOne
