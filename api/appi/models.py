from django.db import models

class Builders(models.Model):
    supplier = models.CharField(max_length=100)
    builder = models.CharField(max_length=100)
    additional_field = models.CharField(max_length=100, default='default value')
    additional_field2 = models.CharField(max_length=100, default='default value')


    # Other fields remain the same

    def __str__(self):
        return self.builder

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name
