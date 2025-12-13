from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Subscriber
from .serializers import SubscriberSerializer

# ---------------------------------------------
# List & Create Subscribers
# ---------------------------------------------
class SubscriberListCreateView(generics.ListCreateAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return subscribers belonging to the logged-in user (owner)
        return Subscriber.objects.filter(owner=self.request.user)
