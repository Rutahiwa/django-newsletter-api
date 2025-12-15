from rest_framework import generics, permissions
from .models import Newsletter
from .serializers import NewsletterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.notify import NotifyService
send_sms = NotifyService.send_sms
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

class NewsletterSendView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            newsletter = Newsletter.objects.get(pk=pk)
        except Newsletter.DoesNotExist:
            return Response({"error": "Newsletter not found"}, status=status.HTTP_404_NOT_FOUND)

        results = []
        for subscriber in newsletter.recipients.all():
            result = send_sms(subscriber.phone_number, newsletter.message)
            results.append({
                "phone_number": subscriber.phone_number,
                "result": result
            })

        return Response({"success": True, "results": results})