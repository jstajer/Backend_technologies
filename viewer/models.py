from django.db import models
from django.db.models import *


class Genre(Model):
    name = CharField(max_length=16, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"<Genre: {self.name}"


class Movie(Model):
    title = CharField(max_length=128, null=False, blank=False)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __repr__(self):
        return (f"<Movie: {self.title}>")

    def __str__(self):
        return f"{self.title} ({self.released})"