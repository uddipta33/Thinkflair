from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50, null=False,blank=False)
    email = models.EmailField(max_length=50)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def num_books(self):
        return self.book_set.count()

    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
