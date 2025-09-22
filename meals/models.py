from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField(help_text='Calories per serving (kcal)')
    protein = models.FloatField(help_text='Protein per serving (g)')
    carbs = models.FloatField(help_text='Carbs per serving (g)')
    fats = models.FloatField(help_text='Fats per serving (g)')

    def __str__(self):
        return self.name

class MealLog(models.Model):
    MEAL_TYPES = [
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('snacks','Snacks'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    quantity = models.FloatField(default=1.0)  # number of servings
    date = models.DateField(auto_now_add=True)

    @property
    def total_calories(self):
        return self.food.calories * self.quantity

    @property
    def total_protein(self):
        return self.food.protein * self.quantity

    @property
    def total_carbs(self):
        return self.food.carbs * self.quantity

    @property
    def total_fats(self):
        return self.food.fats * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.food.name} x{self.quantity}"
