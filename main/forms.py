from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.CharField(label='E-mail')
    adress = forms.CharField(label='Адрес')
