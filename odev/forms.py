from django import forms
from odev.models import Recipe, Ingredient, Like
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class RecipeForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image', 'difficulty', 'ingredients']
