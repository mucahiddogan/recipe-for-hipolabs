from django.shortcuts import render, get_object_or_404,redirect

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe, Ingredient, Like, User
from .forms import RecipeForm, NewUserForm, IngredientForm

from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *

from django.http import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy



def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-time')
    query = request.GET.get('q')
    if query:
        # usernamess = User.objects.get(username=query)
        # print(usernamess)
        recipes = recipes.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(difficulty__icontains=query)
        )

    paginator = Paginator(recipes, 4)
    page = request.GET.get('page')
    recipes = paginator.get_page(page)

    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    context ={
        "object_list": recipes,
        "title": "List"
    }
    return render(request, 'odev/recipe_list.html', {'recipes' : recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'odev/recipe_detail.html', {'recipe': recipe})
   


def recipe_new(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('/')
        else:
            form = RecipeForm()

    else:
        form = RecipeForm()
    return render(request, 'odev/recipe_edit.html', {'form': form})

# class IngredientList(ListView):
#     model = Ingredient

def ingredient_list(request, template_name='odev/ingredient_list.html'):
    ingredient = Ingredient.objects.all()
    data = {}
    data['object_list'] = ingredient
    return render(request, template_name, data)


# classlar, fonksiyonlara göre daha rahat yazıldı
class IngredientNew(CreateView): 
    model = Ingredient
    fields = ['ingredient']
    success_url = reverse_lazy('recipe_new')


class RecipeUpdate(UpdateView): 
    model = Recipe
    fields = ['ingredients', 'name', 'description', 'image', 'difficulty']
    success_url = reverse_lazy('recipe_list')

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')


def logout_request(request):
    logout(request)
    return redirect('/')



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form = AuthenticationForm()                
        else:
            form = AuthenticationForm()

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})


def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request,'registration/register.html',{'form':form})
    
    