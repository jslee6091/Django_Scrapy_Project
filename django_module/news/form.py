from django import forms

class ItDataSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')