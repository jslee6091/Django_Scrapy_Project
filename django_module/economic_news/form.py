from django import forms

class DataForm(forms.Form):
    pass

class DataSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
