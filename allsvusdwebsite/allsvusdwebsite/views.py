from django.views import generic
from django.shortcuts import render

from .models import QuickLinkCardInfo


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')  

def donate(request):
    return render(request, 'fundraising.html')

# def home(request):
#     return render(request, 'index.html')

class QuickLinkCardInfoView(generic.DetailView):
    model = QuickLinkCardInfo
    # context_object_name = 'animal'
    template_name = 'quick_link_card.html'
