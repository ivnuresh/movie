from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('<int:id>/', views.get_id, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update_movie'),
    path('delete/<int:id>/', views.delete, name='delete_movie'),


]