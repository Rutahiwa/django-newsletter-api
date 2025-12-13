from django.urls import path
from .views import NewsletterListCreateView, NewsletterRetrieveUpdateDeleteView

urlpatterns = [
    path('', NewsletterListCreateView.as_view(), name='newsletter-list-create'),
    path('<int:pk>/', NewsletterRetrieveUpdateDeleteView.as_view(), name='newsletter-detail'),
]
