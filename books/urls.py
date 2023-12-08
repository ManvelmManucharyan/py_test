from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    
    path('get_all/', views.get_all_books),
    # path('<int:pk>/', views.author),
]