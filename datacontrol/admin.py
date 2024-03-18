from django.contrib import admin
from .models import Book, Autor

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ['code_book','name_book', 'description', 'categories']  
    list_display_links = ['code_book']
    search_fields = ['name_book', 'autor__name_autor'] 
    list_per_page = 20

class AutorAdmin(admin.ModelAdmin):
    list_display = ['name_autor', 'resume', 'date_born']  
    inlines = [BookInline]
    list_editable = ['resume', 'date_born']  
    list_display_links = ['name_autor']
    search_fields = ['name_autor']  
    list_per_page = 20

admin.site.register(Book, BookAdmin)
admin.site.register(Autor, AutorAdmin)