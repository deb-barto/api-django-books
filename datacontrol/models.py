from django.db import models

class Autor(models.Model):
    name_autor = models.CharField(max_length=30)
    resume = models.CharField(max_length=500)
    date_born = models.DateField()

    def __str__(self):
        return self.name_autor

class Book(models.Model):
    CATEGORIES = (
        ('A', 'Drama'),
        ('B', 'Romance'),
        ('C', 'Ficção'),
    )
    code_book = models.CharField(max_length=30)
    name_book = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    categories = models.CharField(max_length=1, choices=CATEGORIES, default='B')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name_book