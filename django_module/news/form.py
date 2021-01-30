from django import forms

class ItSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class ItRefreshForm(forms.Form):
    pass
