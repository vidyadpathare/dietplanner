from math import floor

def calculate_calorie_goal(profile):
    # Mifflin-St Jeor BMR
    if not (profile.weight and profile.height and profile.age):
        return 2000  # fallback if profile incomplete

    if profile.gender == 'male':
        bmr = 10 * profile.weight + 6.25 * profile.height - 5 * profile.age + 5
    else:
        bmr = 10 * profile.weight + 6.25 * profile.height - 5 * profile.age - 161

    adjust = {'lose': -500, 'gain': 500, 'maintain': 0}
    goal = bmr + adjust.get(profile.goal, 0)
    return max(1200, round(goal))  # safe minimum

def generate_meal_plan(calorie_goal):
    distribution = {'breakfast': 0.25, 'lunch': 0.35, 'dinner': 0.30, 'snacks': 0.10}
    plan = {}
    for meal, pct in distribution.items():
        cals = round(calorie_goal * pct)
        protein_kcal = cals * 0.20
        carbs_kcal = cals * 0.50
        fats_kcal = cals * 0.30
        plan[meal] = {
            'calories': cals,
            'protein_g': floor(protein_kcal / 4),
            'carbs_g': floor(carbs_kcal / 4),
            'fats_g': floor(fats_kcal / 9),
            'example': 'Oats + Milk' if meal == 'breakfast' else ('Chicken + Rice' if meal == 'lunch' else 'Chapati + Veg' if meal == 'dinner' else 'Fruit / Nuts')
        }
    return plan
