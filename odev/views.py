from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.http import *

class RecipeListView(ListView):

    model = Recipe
    paginate_by = 2  # if pagination is desired
    template_name = '/'


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'odev/recipe_list.html', {'recipes' : recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'odev/recipe_detail.html', {'recipe': recipe})


def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('recipe_detail', pk=post.pk)
    else:
        form = RecipeForm()
    return render(request, 'odev/recipe_edit.html', {'form': form})


