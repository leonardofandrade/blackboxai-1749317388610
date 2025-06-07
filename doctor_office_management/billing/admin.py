from django.contrib import admin
from .models import Receipt, Payment, Patient, RecurringBilling

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'date', 'amount', 'created_at')
    search_fields = ('patient_name', 'description')
    list_filter = ('date', 'created_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payee', 'date', 'amount', 'payment_method', 'created_at')
    search_fields = ('payee', 'description')
    list_filter = ('date', 'payment_method', 'created_at')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date_of_birth', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('created_at',)

@admin.register(RecurringBilling)
class RecurringBillingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'frequency', 'amount', 'start_date', 'end_date')
    search_fields = ('patient__full_name', 'description')
    list_filter = ('frequency', 'start_date', 'created_at')
