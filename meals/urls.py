from django.urls import path
from . import views

app_name = 'meals'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/add/', views.add_food, name='add_food'),
    path('meals/add/', views.add_meal_log, name='add_meallog'),
]
