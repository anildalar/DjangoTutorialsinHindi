from django.db import models

# Create your models here.


class Brand(models.Model):# PacalCase
    brand_name = models.CharField(max_length=255)
    pass