from rest_framework import serializers
from datacontrol.models import Autor, Book

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    autor_name = serializers.CharField(source='autor.name_autor', read_only=True) 
    
    class Meta:
        model = Book
        fields = '__all__' 

    def get_categories(self, obj):
        return obj.get_categories_display()