import requests
from django.shortcuts import render
from django.conf import settings

def search_recipes(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        url = "https://api.spoonacular.com/recipes/complexSearch"
        params = {
            'apiKey': settings.SPOONACULAR_API_KEY,
            'query': query,
            'number': 10
        }
        response = requests.get(url, params=params)
        data = response.json()
        recipes = data.get('results', [])
        return render(request, 'finder/results.html', {'recipes': recipes})
    return render(request, 'finder/search.html')

def recipe_detail(request, recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {'apiKey': settings.SPOONACULAR_API_KEY}
    response = requests.get(url, params=params)
    recipe = response.json()
    return render(request, 'finder/detail.html', {'recipe': recipe})