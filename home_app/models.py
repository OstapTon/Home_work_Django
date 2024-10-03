from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
