from django.urls import path
from .views import NewsletterListCreateView, NewsletterRetrieveUpdateDeleteView, NewsletterSendView

urlpatterns = [
    path('', NewsletterListCreateView.as_view(), name='newsletter-list-create'),
    path('<int:pk>/', NewsletterRetrieveUpdateDeleteView.as_view(), name='newsletter-detail'),
    path('<int:pk>/send/', NewsletterSendView.as_view(), name='newsletter-send'),
]
