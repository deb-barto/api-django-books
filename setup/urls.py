from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from datacontrol.views import BookViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'livros', BookViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
