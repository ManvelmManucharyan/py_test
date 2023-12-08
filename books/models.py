from django.db import models
from authors.models import Author

class Book(models.Model):
  title = models.CharField(max_length=255)
  year = models.IntegerField()
  category = models.CharField(max_length=255, default="Any")
  pageCount = models.IntegerField(default=0)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title