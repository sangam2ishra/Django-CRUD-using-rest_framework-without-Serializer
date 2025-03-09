from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'description', 'category', 'price', 'brand', 'quantity']

    def clean_quantity(self):
        quantity=self.cleaned_data.get('quantity')
        if quantity is None or quantity<=10:
            raise forms.ValidationError('Quantity must be more than 10')
        return quantity
    
    def clean_price(self):
        price=self.cleaned_data.get('price')
        if price is None or price>1000:
            raise forms.ValidationError('Price must be less than 1000')
        return price