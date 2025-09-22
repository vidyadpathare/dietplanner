from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Food, MealLog
from .forms import FoodForm, MealLogForm
from .utils import calculate_calorie_goal, generate_meal_plan

@login_required
def dashboard(request):
    profile = request.user.userprofile
    calorie_goal = calculate_calorie_goal(profile)
    plan = generate_meal_plan(calorie_goal)

    today = timezone.now().date()
    logs = MealLog.objects.filter(user=request.user, date=today)
    consumed = sum(log.total_calories for log in logs)
    remaining = calorie_goal - consumed

    context = {
        'calorie_goal': calorie_goal,
        'plan': plan,
        'logs': logs,
        'consumed': consumed,
        'remaining': remaining
    }
    return render(request, 'meals/dashboard.html', context)

@login_required
def food_list(request):
    q = request.GET.get('q', '')
    foods = Food.objects.filter(name__icontains=q).order_by('name')
    return render(request, 'meals/food_list.html', {'foods': foods, 'q': q})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals:food_list')
    else:
        form = FoodForm()
    return render(request, 'meals/add_food.html', {'form': form})

@login_required
def add_meal_log(request):
    if request.method == 'POST':
        form = MealLogForm(request.POST)
        if form.is_valid():
            ml = form.save(commit=False)
            ml.user = request.user
            ml.save()
            return redirect('meals:dashboard')
    else:
        form = MealLogForm()
    return render(request, 'meals/add_meallog.html', {'form': form})
