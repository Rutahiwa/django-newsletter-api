from rest_framework import serializers
from .models import Newsletter
from subscribers.models import Subscriber  

class NewsletterSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(read_only=True)
    recipients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Subscriber.objects.all(),
        required=False,
        default=None
    )

    class Meta:
        model = Newsletter
        fields = '__all__'

    def create(self, validated_data):
        # Assign the logged-in user automatically
        validated_data['admin'] = self.context['request'].user
        # If `recipients` is omitted in the request, default to all subscribers
        # that belong to the creating user. If `recipients` is provided as
        # an empty list, respect that and set no recipients.
        recipients_data = validated_data.pop('recipients', None)
        newsletter = super().create(validated_data)

        if recipients_data is None:
            # Use all subscribers owned by the admin creating this newsletter
            owner = self.context['request'].user
            recipients_qs = Subscriber.objects.filter(owner=owner)
            newsletter.recipients.set(recipients_qs)
        else:
            newsletter.recipients.set(recipients_data)
        return newsletter

    def update(self, instance, validated_data):
        # If recipients not provided, do not modify existing recipients.
        recipients_data = validated_data.pop('recipients', None)
        newsletter = super().update(instance, validated_data)
        if recipients_data is not None:
            newsletter.recipients.set(recipients_data)
        return newsletter
