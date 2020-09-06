from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
age_chs=[(0,0),(6,6),(12,12),(15,15),(18,18)]
class Genre(models.Model):
    name=models.CharField(max_length=20,unique=True)
    age_limit=models.IntegerField(choices=age_chs)

    def __str__(self):
        return self.name

class Director(models.Model):
    name=models.CharField(max_length=20,null=True)
    surname=models.CharField(max_length=30)
    country=models.CharField(max_length=30)

    class Meta:
        unique_together=("name","surname")

    def __str__(self):
        return f"{self.name}  {self.surname} from {self.country}"

class Country(models.Model):
    name=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title=models.CharField(max_length=100)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10),MinValueValidator(1)]
    )
    released = models.DateField(null=True)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    genre=models.ForeignKey(Genre,null=True,on_delete=models.SET_NULL)
    director=models.ForeignKey(Director,null=True,on_delete=models.SET_NULL)
    countrys=models.ManyToManyField(Country,related_name='Movie')

    class Meta:
        unique_together=("title","released","director")

    def __str__(self):
        return f"{self.title} from {self.released}"