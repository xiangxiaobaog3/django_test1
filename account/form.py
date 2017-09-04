from django import forms


class ALogin(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    ip = forms.GenericIPAddressField()