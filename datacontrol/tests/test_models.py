
from django.test import TestCase
from datacontrol.models import Autor, Book
from datetime import date

class AutorModelTest(TestCase):

    def test_create_autor(self):
        autor = Autor.objects.create(
            name_autor='Autor Exemplo',
            resume='Um resumo de teste.',
            date_born=date.today()
        )
        self.assertEqual(autor.name_autor, 'Autor Exemplo')
        self.assertEqual(autor.resume, 'Um resumo de teste.')
        self.assertEqual(autor.date_born, date.today())

class BookModelTest(TestCase):

    def setUp(self):
        self.autor = Autor.objects.create(
            name_autor='Autor para Livro',
            resume='Um resumo de teste para livro.',
            date_born=date.today()
        )

    def test_create_book(self):
        book = Book.objects.create(
            code_book='001',
            name_book='Livro de Teste',
            description='Descrição do livro de teste.',
            categories='A',
            autor=self.autor
        )
        self.assertEqual(book.code_book, '001')
        self.assertEqual(book.name_book, 'Livro de Teste')
        self.assertEqual(book.description, 'Descrição do livro de teste.')
        self.assertEqual(book.categories, 'A')
        self.assertEqual(book.autor, self.autor)
        self.assertEqual(book.autor.name_autor, 'Autor para Livro')