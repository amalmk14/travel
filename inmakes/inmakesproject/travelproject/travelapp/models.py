from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class teams(models.Model):
    teamsname=models.CharField(max_length=100)
    teamsimg=models.ImageField(upload_to='photos')
    teamsdesc=models.TextField()

    def __str__(self):
        return self.teamsname


