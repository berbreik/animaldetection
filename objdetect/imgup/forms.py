from django import forms
class imageuploadform(forms.Form):
    image= forms.ImageField()