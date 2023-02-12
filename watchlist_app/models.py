from django.db import models

class Movie (models.Model):
   name  = models.CharField(max_length=50, help_text="the title of the movie ", default="Title")
   description = models.CharField(max_length=200, default="description ")
   active=models.BooleanField(default=True)


   def __str__(self):
       return self.name

