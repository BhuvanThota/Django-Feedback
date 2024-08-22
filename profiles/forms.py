from django import forms


class PorfileForm(forms.Form):
    user_image = forms.ImageField()
