from django.db import models

# Create your models here.
class LmsPublic(models.Model):
    type_holiday = models.CharField(max_length=300,null=False)
    created_at = models.DateField(null=False)
    name = models.CharField(max_length=300,null=False)
    country = models.CharField(max_length=300,null=False)

