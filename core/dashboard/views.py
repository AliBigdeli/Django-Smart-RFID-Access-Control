from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

class IndexView(LoginRequiredMixin,TemplateView):
    """
    a class based view to show home page
    """

    template_name = "dashboard/home.html"
    
    
class CardIDManagement(LoginRequiredMixin,TemplateView):
    """
    a class based view to show home page
    """

    template_name = "dashboard/card-management.html"
    

class CardReaderManagement(LoginRequiredMixin,TemplateView):
    """
    a class based view to show home page
    """

    template_name = "dashboard/reader-management.html"
    

class CardReaderLogs(LoginRequiredMixin,TemplateView):
    """
    a class based view to show home page
    """

    template_name = "dashboard/reader-logs.html"