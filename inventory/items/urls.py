from django.urls import path

from items import views

urlpatterns = [
    path('', views.items, name='items'),
    path('edit/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
