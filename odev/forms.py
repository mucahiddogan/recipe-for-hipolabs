from django import forms
from odev.models import Recipe, Ingredient, Like
#from django.contrib.auth.models import User

#class RecipeForm(forms.Form):
 #   name = forms.CharField(label='name', max_length=100)

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['user', 'name', 'description','image', 'difficulty', 'ingredients']

    #def __init__(self, *args, **kwargs):
     #   super(RecipeForm, self).__init__(*args, **kwargs)
      #  self.fields['image'].required = False