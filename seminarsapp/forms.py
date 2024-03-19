from datetime import date
from django import forms


class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=100, widget=forms.TextInput())
    product_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    product_price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput())
    product_count = forms.IntegerField(widget=forms.NumberInput())
    product_date_added = forms.DateField(initial=date.today(), widget=forms.DateInput(attrs={'type': 'date'}))
    product_image = forms.ImageField(widget=forms.FileInput())


class AddImage(forms.Form):
    image = forms.ImageField(widget=forms.FileInput())
