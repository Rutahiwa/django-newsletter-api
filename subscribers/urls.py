from django.urls import path
from .views import SubscriberListCreateView

urlpatterns = [
    path("", SubscriberListCreateView.as_view(), name="subscriber-list-create"),
]
