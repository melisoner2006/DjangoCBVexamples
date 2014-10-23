# Create your views here.
from django.views.generic import TemplateView, CreateView, View, ListView
from django.views.generic.base import RedirectView
from .form import ContactForm
from .models import Contact

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

class homePage(TemplateView):
    template_name = 'home.html'
    
class NewContact(CreateView):
    template_name = 'createcontact.html'
    form = ContactForm()
    model  = Contact
    success_url ='.'
        
    def get_context_data(self, **kwargs):
        context = ({
            'form': self.form
            
        })
        return context  

class MyView(View):
    
    def get(self, request):
        return HttpResponse("Hello, World!")

class ListContactView(ListView):
    model = Contact
    
class ContactRedirectView(RedirectView):
    permanent = False
    query_string = False
    
    def get_redirect_url(self, pk):
        contact = get_object_or_404(Contact, pk=pk)
        contact.update_count()
        return reverse('contact-detail', args = (pk,))
        
    
                    