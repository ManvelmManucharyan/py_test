from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  nationality = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name