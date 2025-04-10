from django.urls import path
from . import views

app_name = 'vc_app'

urlpatterns = [
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/create/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    path('virtual-cards/', views.VirtualCardListView.as_view(), name='virtual_card_list'),
    path('virtual-cards/create/<int:invoice_id>/', views.create_virtual_card, name='virtual_card_create'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transactions/pay/<int:card_id>/', views.create_transaction, name='transaction_create'),
] 