from datetime import date
from django import forms
from .models import Product


class AddProductForm(forms.Form):
    product_name = forms.CharField(template_name='Название товара', max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_description = forms.CharField(template_name='Описание товара',
                                          widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))
    product_price = forms.DecimalField(template_name='Стоимость товара', max_digits=8, decimal_places=2,
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_count = forms.IntegerField(template_name='Количество товара',
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_date_added = forms.DateField(template_name='Дата добавления товара', initial=date.today(),
                                         widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    product_image = forms.ImageField(template_name='Изображение товара',
                                     widget=forms.FileInput(attrs={'class': 'form-control'}))

# class AddProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
