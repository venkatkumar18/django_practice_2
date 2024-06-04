from django import forms
from .views import Items

class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Items 
        fields = ('name','description','price','image','category', 'created_by')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('name','description','price','image','category', 'created_by')