from django.contrib import admin
from django_project.genre_app.models import Genre

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)