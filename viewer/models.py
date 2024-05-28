from django.db import models
from django.db.models import *


class Genre(Model):
    name = CharField(max_length=16, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f" {self.name}"


class Movie(Model):
    title_orig = CharField(max_length=128, null=False, blank=False)
    #genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    genres = ManyToManyField(Genre, blank=False, related_name='movies_of_genre')
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title_orig']

    def __repr__(self):
        return (f"<Movie: {self.title_orig}>")

    def __str__(self):
        return f"{self.title_orig} ({self.released})"