from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from .models import Invoice, VirtualCard, Transaction
from .forms import InvoiceForm, VirtualCardForm, TransactionForm

# Create your views here.

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'vc_app/invoice_list.html'
    context_object_name = 'invoices'

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'vc_app/invoice_form.html'
    success_url = reverse_lazy('vc_app:invoice_list')

class VirtualCardListView(ListView):
    model = VirtualCard
    template_name = 'vc_app/virtual_card_list.html'
    context_object_name = 'virtual_cards'

def create_virtual_card(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    
    if VirtualCard.objects.filter(invoice=invoice).exists():
        messages.error(request, 'A virtual card already exists for this invoice.')
        return redirect('vc_app:invoice_list')
    
    if request.method == 'POST':
        form = VirtualCardForm(request.POST)
        if form.is_valid():
            virtual_card = form.save(commit=False)
            virtual_card.invoice = invoice
            virtual_card.save()
            messages.success(request, 'Virtual card created successfully.')
            return redirect('vc_app:virtual_card_list')
    else:
        form = VirtualCardForm()
    
    return render(request, 'vc_app/virtual_card_form.html', {
        'form': form,
        'invoice': invoice
    })

class TransactionListView(ListView):
    model = Transaction
    template_name = 'vc_app/transaction_list.html'
    context_object_name = 'transactions'

def create_transaction(request, card_id):
    virtual_card = get_object_or_404(VirtualCard, id=card_id)
    
    # Calculate total amount already paid for this invoice
    total_paid = Transaction.objects.filter(
        virtual_card__invoice=virtual_card.invoice,
        status='success'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    # Calculate remaining amount
    remaining_amount = virtual_card.invoice.amount - total_paid
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.virtual_card = virtual_card
            
            if transaction.amount <= remaining_amount:
                transaction.status = 'success'
                # Check if this payment completes the invoice
                if (total_paid + transaction.amount) >= virtual_card.invoice.amount:
                    virtual_card.invoice.status = 'paid'
                    virtual_card.invoice.save()
                transaction.save()
                messages.success(request, 'Transaction processed successfully.')
            else:
                transaction.status = 'failed'
                messages.error(request, f'Transaction amount exceeds remaining invoice amount. Maximum amount allowed: ${remaining_amount:.2f}')
                transaction.save()
            
            return redirect('vc_app:transaction_list')
    else:
        form = TransactionForm()
    
    return render(request, 'vc_app/transaction_form.html', {
        'form': form,
        'virtual_card': virtual_card,
        'remaining_amount': remaining_amount
    })
