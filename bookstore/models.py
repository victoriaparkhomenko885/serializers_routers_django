from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=48)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    site = models.URLField()

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return f'{self.title} ({self.publication_date})'
