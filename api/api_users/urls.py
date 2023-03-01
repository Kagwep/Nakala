from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    #users - post and get all
    path('users/', UserList.as_view()),
    #users get by id , update delete
    path('users/<int:pk>/', UserDetail.as_view()),
]
