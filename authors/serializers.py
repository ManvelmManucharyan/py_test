from rest_framework import serializers
from .models import Author
from django.forms import ValidationError

class AuthorSerializer(serializers.ModelSerializer):
    description =  serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = "__all__"
        
    def validate(self, data):
        if data["name"] == "Arsen":
            raise ValidationError("No Arsen please")
        return data