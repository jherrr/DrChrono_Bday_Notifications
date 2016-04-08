from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date_published')
