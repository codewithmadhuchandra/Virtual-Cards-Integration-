from django import forms
from .models import Invoice, VirtualCard, Transaction
import datetime

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }

class VirtualCardForm(forms.ModelForm):
    class Meta:
        model = VirtualCard
        fields = ['card_number', 'expiry_date', 'cvv']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'cvv': forms.PasswordInput(),
        }

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']
        if expiry_date < datetime.date.today():
            raise forms.ValidationError("Expiry date cannot be in the past")
        return expiry_date

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        } 