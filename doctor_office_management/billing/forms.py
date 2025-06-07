from django import forms
from .models import Receipt, Payment, Patient, RecurringBilling

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['patient_name', 'date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payee', 'date', 'amount', 'payment_method', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'email', 'phone', 'date_of_birth', 'address', 'notes']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }

class RecurringBillingForm(forms.ModelForm):
    class Meta:
        model = RecurringBilling
        fields = ['patient', 'frequency', 'amount', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
