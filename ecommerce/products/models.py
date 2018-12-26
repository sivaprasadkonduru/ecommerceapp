from django.db import models

# Create your models here.

class Stores(models.Model):

    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_no = models.BigIntegerField()
    landmark = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return "-".join([self.name, self.location])





