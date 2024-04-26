# forms.py

# from django import forms
# from .models import Payment

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['payment_option', 'amount', 'card_number', 'expiry_date', 'cvv', 'phone_number']

from django import forms
import datetime
from .models import Payment

class PaymentForm1(forms.Form):
    PAYMENT_OPTIONS = [
        ('cash','Cash'),
        ('bkash', 'Bkash'),
        ('rocket', 'Rocket'),
        ('mastercard', 'Mastercard'),
    ]
    
    ROOM_TYPES = [
        ('non_ac', 'Non AC'),
        ('ac', 'AC'),
        ('deluxe', 'Deluxe'),
        ('king', 'King'),
        ('queen', 'Queen'),
    ]
    
    CURRENCY_CHOICES = [
        ('taka', 'Taka'),
        ('rupee', 'Rupee'),
        ('dollar', 'Dollar'),
    ]
    
 

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'payment_option', 'amount', 'card_number', 'expiry_date', 'num_rooms', 'cvv', 'phone_number', 'promo_code', 'room_type', 'check_in', 'check_out', 'payment_option_image']
    
#     def clean(self):
#         cleaned_data = super().clean()
#         # Parse and reformat check_in and check_out dates
#         check_in = cleaned_data.get('check_in')
#         check_out = cleaned_data.get('check_out')
#         if check_in and check_out:
#             # Assuming date format is mm/dd/yyyy
#             cleaned_data['check_in'] = datetime.datetime.strptime(check_in, '%m/%d/%Y').date()
#             cleaned_data['check_out'] = datetime.datetime.strptime(check_out, '%m/%d/%Y').date()
#         return cleaned_data


    # payment_option = forms.ChoiceField(choices=PAYMENT_OPTIONS, widget=forms.Select(attrs={'id': 'payment_option'}))
    # room_type = forms.ChoiceField(choices=ROOM_TYPES, widget=forms.Select(attrs={'id': 'room_type'}))
    # currency = forms.ChoiceField(choices=CURRENCY_CHOICES, widget=forms.Select(attrs={'id': 'currency'}))
    # amount = forms.DecimalField(widget=forms.TextInput(attrs={'id': 'amount', 'readonly': True}))
    # card_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'card_number'}))
    # expiry_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'id': 'expiry_date'}))
    # cvv = forms.CharField(max_length=4, required=False, widget=forms.TextInput(attrs={'id': 'cvv'}))
    # phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'id': 'phone_number'}))
    
    
