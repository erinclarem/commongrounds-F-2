from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LocalEvents
# Create your views here.


class LocalEventsListView(ListView):
    model = LocalEvents
    template_name = "localevents_list.html"


class LocalEventsDetailView(LoginRequiredMixin, DetailView):
    model = LocalEvents
    template_name = "localevent_detail.html"
