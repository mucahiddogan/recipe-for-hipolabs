from django.shortcuts import render, get_object_or_404,redirect

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe, Ingredient, Like, User
from .forms import RecipeForm

from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *

from django.http import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class RecipeListView(ListView):

    model = Recipe
    paginate_by = 2  # if pagination is desired
    template_name = '/'


# class UserFormView(View):
#     from_class = UserForm
#     template_name = 'odev/registration/register.html'


#     def get(self, request):
#         form = self.form_class(request.POST)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)

#         if form.is_valid():

#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()

#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
        
        
#         return render(request, self.template_name, {'form': form})



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

    paginator = Paginator(recipes, 5)
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
        

        

    # recipes = Recipe.objects.all()
    # query = request.GET.get('q')
    # paginator = Paginator(recipes, 5)
    # page = request.GET.get('page')
    # recipes = paginator.get_page(page)

    # if query:
    #     recipes = recipes.filter(description__icontains=query) 

    
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
            #post.user = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/')
        else:

            print("asdasdad")   
    else:
        form = RecipeForm()
    return render(request, 'odev/recipe_edit.html', {'form': form})


