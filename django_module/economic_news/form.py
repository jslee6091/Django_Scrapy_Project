from django import forms

class RefreshForm(forms.Form):
    pass


class SearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
