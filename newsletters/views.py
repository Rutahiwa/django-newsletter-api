from rest_framework import generics, permissions
from .models import Newsletter
from .serializers import NewsletterSerializer

class NewsletterListCreateView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        # Pass request to serializer to access request.user
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class NewsletterRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
