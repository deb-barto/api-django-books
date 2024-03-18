from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datacontrol.models import Autor, Book
from datetime import date
from django.contrib.auth.models import User

class AutorAPITests(APITestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            name_autor='Test Autor', 
            resume='Test resume', 
            date_born='2020-01-01'
        )
    def test_create_autor(self):
        url = reverse('autor-list')
        data = {
            'name_autor': 'Novo Test Autor', 
            'resume': 'Novo Test resume', 
            'date_born': '2021-01-01'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)  # Inclui o autor criado no setUp
        self.assertEqual(Autor.objects.latest('id').name_autor, 'Novo Test Autor')

    def test_retrieve_autor(self):
        url = reverse('autor-detail', args=[self.autor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_autor'], 'Test Autor')

    def test_update_autor(self):
        url = reverse('autor-detail', args=[self.autor.id])
        updated_data = {
            'name_autor': 'Atualizado Test Autor', 
            'resume': 'Atualizado Test resume', 
            'date_born': '2022-01-01'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.autor.refresh_from_db()
        self.assertEqual(self.autor.name_autor, 'Atualizado Test Autor')

    def test_delete_autor(self):
        url = reverse('autor-detail', args=[self.autor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Autor.objects.count(), 0)
class BookAPITests(APITestCase):
    def setUp(self):
        self.autor = Autor.objects.create(name_autor='Autor Teste', resume='Biografia Teste', date_born=date.today())
        self.book_data = {
            "code_book": "001",
            "name_book": "Livro Teste",
            "description": "Descrição do Livro Teste",
            "categories": "A",
            "autor": self.autor
        }

    def test_retrieve_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('Book-detail', args=[book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_book'], book.name_book)

    def test_create_book(self):
        url = reverse('Book-list')
        data = self.book_data.copy()
        data['autor'] = self.autor.id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().name_book, 'Livro Teste')

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = self.book_data.copy()
        updated_data['name_book'] = "Livro Teste Atualizado"
        updated_data['autor'] = self.autor.id
        url = reverse('Book-detail', args=[book.id])
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.name_book, "Livro Teste Atualizado")

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('Book-detail', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())