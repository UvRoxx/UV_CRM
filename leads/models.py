from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Getting a phone number field that respects the E.164 Will help later with SMS Automation Integration
# https://en.wikipedia.org/wiki/E.164
# https://github.com/stefanfoulis/django-phonenumber-field


# class User(AbstractUser):
#     pass


class Lead(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=400)
    email = models.EmailField(max_length=50, null=True)
    number = PhoneNumberField(blank=True, null=True)
    contacted = models.BooleanField(default=False)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
