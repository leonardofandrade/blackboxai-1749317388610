from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Receipt, Payment, Patient, RecurringBilling
from .forms import ReceiptForm, PaymentForm, PatientForm, RecurringBillingForm

class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'billing/receipt_list.html'
    context_object_name = 'receipts'

class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'billing/receipt_form.html'
    success_url = reverse_lazy('receipt_list')

class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'billing/receipt_form.html'
    success_url = reverse_lazy('receipt_list')

class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    model = Receipt
    template_name = 'billing/receipt_confirm_delete.html'
    success_url = reverse_lazy('receipt_list')

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'billing/payment_list.html'
    context_object_name = 'payments'

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'billing/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'billing/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    template_name = 'billing/payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'billing/patients/list.html'
    context_object_name = 'patients'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'billing/patients/form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'billing/patients/form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'billing/patients/confirm_delete.html'
    success_url = reverse_lazy('patient_list')

class RecurringBillingListView(LoginRequiredMixin, ListView):
    model = RecurringBilling
    template_name = 'billing/recurring/list.html'
    context_object_name = 'recurring_billings'

class RecurringBillingCreateView(LoginRequiredMixin, CreateView):
    model = RecurringBilling
    form_class = RecurringBillingForm
    template_name = 'billing/recurring/form.html'
    success_url = reverse_lazy('recurring_list')

class RecurringBillingUpdateView(LoginRequiredMixin, UpdateView):
    model = RecurringBilling
    form_class = RecurringBillingForm
    template_name = 'billing/recurring/form.html'
    success_url = reverse_lazy('recurring_list')

class RecurringBillingDeleteView(LoginRequiredMixin, DeleteView):
    model = RecurringBilling
    template_name = 'billing/recurring/confirm_delete.html'
    success_url = reverse_lazy('recurring_list')
