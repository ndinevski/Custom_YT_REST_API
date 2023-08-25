from django import forms

class handle_form(forms.Form):
   handle = forms.CharField(max_length=1000)
 