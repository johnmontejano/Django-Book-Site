from django.urls import path

from . import views
app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.detail, name='detail')
]