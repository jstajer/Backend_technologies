from django.db import models
from django.db.models import *


class Genre(Model):
    name = CharField(max_length=16)

    def __str__(self):
        return f"<Genre: {self.name}"


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __repr__(self):
        return (f"<Movie: {self.title}>")

    def __str__(self):
        return f"{self.title} ({self.released})"