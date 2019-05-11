from django.core.paginator import Paginator
from django.shortcuts import render


def listing(request):
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    recipes = paginator.get_page(page)
    return render(request, 'recipe_list.html', {'recipes': recipes})