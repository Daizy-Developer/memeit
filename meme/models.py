from django.db import models
MEME_CHOICES = (
    ("The Classics", "The Classics"),
    ("The Trenders", "The Trenders"),
    ("The One-Hit Wonder", "The One-Hit Wonder"),
    ("The Social Media", "The Social Media"),
    ("The Series", "The Series"),
    ("The Niche", "The Niche"),
    ("The Obscurity", "The Obscurity"),
    ("The Comics", "The Comics"),
    ("Other","Other"),
    )
# Create your models here.
class Categorie(models.Model):
    Category = models.CharField(max_length = 30,choices = MEME_CHOICES)
    Date = models.DateField()
    Time =  models.TimeField()
    def __str__(self):
        return self.Category

class Meme(models.Model):
    Memename = models.CharField(max_length=30)
    Caption =  models.CharField(max_length=200)
    Image =  models.ImageField(upload_to="memes")
    Category = models.ForeignKey(Categorie , on_delete=models.CASCADE)
    Date = models.DateField()
    Time =  models.TimeField()
    def __str__(self):
        return self.Memename


