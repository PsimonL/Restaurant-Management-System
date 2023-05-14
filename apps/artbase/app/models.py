from django.db import models

class Artist(models.Model):
    artist_name = models.CharField('Artist Name', max_length=30)

class Artwork(models.Model):
    pass

class GroupOfArtworks(models.Model):
    pass

class Customer(models.Model):
    pass

class Transactions(models.Model):
    pass