from django.db import models
from django.conf import settings
from subscribers.models import Subscriber


class Newsletter(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="newsletters"
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    recipients = models.ManyToManyField(Subscriber)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
