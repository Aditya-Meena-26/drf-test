from django.db import models
from django.core.exceptions import ValidationError
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    
    def clean(self):
        if self.books.count() > 5:
            raise ValidationError('An author cannot have more than 5 books.')

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    
    