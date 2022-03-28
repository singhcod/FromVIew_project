from django.shortcuts import render
from django.views.generic import FormView

from .forms import Contactform

# Create your views here.
class ContactView(FormView):
    template_name = 'school/contact.html'
    form_class = Contactform