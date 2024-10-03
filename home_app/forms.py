from django import forms
from home_app.models import Client, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['registration_date'] = forms.DateTimeField(
                initial=self.instance.registration_date,
                widget=forms.TextInput(attrs={'readonly': 'readonly'})
            )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['added_date'] = forms.DateTimeField(
                initial=self.instance.add_date,
                widget=forms.TextInput(attrs={'readonly': 'readonly'})
            )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount']
        widgets = {
            'products': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            if self.instance and self.instance.pk:
                self.fields['order_date'] = forms.DateTimeField(
                    initial=self.instance.add_date,
                    widget=forms.TextInput(attrs={'readonly': 'readonly'})
                )
