from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Phones(models.Model):
    phonenumber = models.CharField(max_length=255)
    phonetype = models.CharField(max_length=255)
