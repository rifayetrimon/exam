from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.db.models import Q

########### show all contacts
def contact_list(request):
    search_query = request.GET.get('search', '')
    contacts = Contact.objects.filter(
        Q(first_name__icontains=search_query) | Q(email__icontains=search_query)
    )
    return render(request, 'contact_list.html', {'contacts': contacts})

#############Add contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

################ View contact details
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

#################Edit contact details
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

############### Delete contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_contact.html', {'contact': contact})