from rest_framework import serializers
from .models import Book
from authors.models import Author

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
