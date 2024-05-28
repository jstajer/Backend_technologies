from django.db.models import *


class Genre(Model):
    name = CharField(max_length=16, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f" {self.name}"

    def movies_count(self):
        return self.movies.all().count()

class Country(Model):
    name = CharField(max_length=16, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f" {self.name}"


class Movie(Model):
    title_orig = CharField(max_length=128, null=False, blank=False)
    title_cz = CharField(max_length=128, null=True, blank=False)
    countries = ManyToManyField(Country, blank=True)
    #genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    genres = ManyToManyField(Genre, blank=False, related_name='movies_of_genre')
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
    length = IntegerField(null = True)




    class Meta:
        ordering = ['title_orig']

    def __repr__(self):
        return (f"<Movie: {self.title_orig}>")

    def __str__(self):
        return f"{self.title_orig} ({self.released})"

    def print_genres(self):
        result = ""
        for genre in self.genres.all():
            result += f"{genre}, "
        return result[:-2]


# TODO: People
"""
- name
- surname
- date_of_birth
- date_of_death
- place_of_birth
- place_of_death
- country
- biography
- status
"""
# TODO: actors
# TODO: directors