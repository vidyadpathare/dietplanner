from django import forms
from .models import Food, MealLog

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','calories','protein','carbs','fats']

class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['food','meal_type','quantity']
