from django.urls import path
from .views import AuthorCreate, AuthorList, AuthorDetail

urlpatterns = [
    path('create/', AuthorCreate.as_view()),
    
    path('get_all/', AuthorList.as_view()),
    path('<int:pk>/', AuthorDetail.as_view()),
]