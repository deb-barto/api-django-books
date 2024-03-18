from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datacontrol.models import Autor, Book
from datetime import date

class AutorViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.autor = Autor.objects.create(name_autor='Test Autor', resume='Um resumo', date_born=date.today())

    def test_autor_list(self):
        url = reverse('autor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_autor_detail(self):
        url = reverse('autor-detail', args=[self.autor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_autor'], 'Test Autor')

    def test_autor_livros(self):
        Book.objects.create(
            autor=self.autor,
            code_book='001',
            name_book='Test Book',
            description='Test Description',
            categories='A'
        )
        url = reverse('autor-livros', args=[self.autor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class BookViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.autor = Autor.objects.create(name_autor='Another Test Autor', resume='Outro resumo', date_born=date.today())
        cls.book = Book.objects.create(
            autor=cls.autor,
            code_book='002',
            name_book='Another Test Book',
            description='Another Test Description',
            categories='B'
        )

    def test_Book_list(self):
        url = reverse('Book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_Book_detail(self):
        url = reverse('Book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_book'], 'Another Test Book')