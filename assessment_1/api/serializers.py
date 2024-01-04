from rest_framework import serializers

from .models import Author,Book

#serializers
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        author = data['author']
        if author.num_books<5:
            return data
        else:
            raise serializers.ValidationError({"validation_error":"An author cannot have more than 5 books"})

