from django.urls import path
from .views import LocalEventsListView, LocalEventsDetailView
urlpatterns = [
    path('localevents/list', LocalEventsListView.as_view(), name='localevents_list'),
    path('localevents/event/<int:pk>/',
         LocalEventsDetailView.as_view(), name='localevent_detail'),
]

app_name = 'localevents'
