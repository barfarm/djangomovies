from django.contrib import admin

# Register your models here.
from core.models import Movie
from core.models import Genre
from core.models import Director


#
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
