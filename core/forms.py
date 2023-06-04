from django import forms


class BookNameFilter(forms.Form):
    name = forms.CharField()
