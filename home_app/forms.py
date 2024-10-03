# forms.py
from django import forms
from home_app.models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'phone_number', 'address', 'registration_date']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity', 'added_date']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount', 'order_date']
        widgets = {
            'product': forms.CheckboxSelectMultiple(),  # Для отображения поля ManyToMany в виде чекбоксов
        }
