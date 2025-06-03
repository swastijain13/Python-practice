from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    skills = models.JSONField()  
    employer = models.CharField(max_length=100)

    def __str__(self):
        return self.name