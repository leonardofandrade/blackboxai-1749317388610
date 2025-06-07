from django.urls import path
from . import views

urlpatterns = [
    # Dashboard (using Receipt list as dashboard)
    path('', views.ReceiptListView.as_view(), name='receipt_list'),
    
    # Receipt URLs
    path('receipts/', views.ReceiptListView.as_view(), name='receipt_list'),
    path('receipts/create/', views.ReceiptCreateView.as_view(), name='receipt_create'),
    path('receipts/<int:pk>/update/', views.ReceiptUpdateView.as_view(), name='receipt_update'),
    path('receipts/<int:pk>/delete/', views.ReceiptDeleteView.as_view(), name='receipt_delete'),
    
    # Payment URLs
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/create/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/update/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),

    # Patient URLs
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),

    # Recurring Billing URLs
    path('recurring/', views.RecurringBillingListView.as_view(), name='recurring_list'),
    path('recurring/create/', views.RecurringBillingCreateView.as_view(), name='recurring_create'),
    path('recurring/<int:pk>/update/', views.RecurringBillingUpdateView.as_view(), name='recurring_update'),
    path('recurring/<int:pk>/delete/', views.RecurringBillingDeleteView.as_view(), name='recurring_delete'),
]
