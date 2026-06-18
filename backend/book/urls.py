from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend.book.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
	path('', include(router.urls)),
]