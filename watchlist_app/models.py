from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# chabter 5:update module


# this table for add the website for this movie like netlfix
class StreamPlatform (models.Model):
    name = models.CharField(max_length=30,)
    about = models.CharField(max_length=150, )
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

# this table for add movie


class WatchList (models.Model):
    tital = models.CharField(max_length=50, help_text="the title of the movie ", default="Title")
    plateform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="WatchList")
    storyline = models.CharField(max_length=200, default="description ")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    number_rating=models.IntegerField(default=0)
    avg_rating=models.FloatField(default=0)

    def __str__(self):
        return self.tital

# 5:Serializer Relations Continued
# table to add review to the movie every movie hav mult review
class Review (models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True )
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE, related_name="Review")
    
    def __str__(self):
        return str(self.rating)+" ----> " + str(self.watchlist)


# berfor chabter 5:update module
class Movie (models.Model):
    name = models.CharField(
    max_length=50, help_text="the title of the movie ", default="Title")
    description = models.CharField(max_length=200, default="description ")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
