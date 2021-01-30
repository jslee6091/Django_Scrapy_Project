from django import forms

class WorldSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class WorldRefreshForm(forms.Form):
    pass
