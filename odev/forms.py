from django import forms

from .models import Recipe, Ingredient, Like

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'description','image','difficulty','ingredients')