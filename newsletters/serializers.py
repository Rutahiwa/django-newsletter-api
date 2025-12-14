from rest_framework import serializers
from .models import Newsletter
from subscribers.models import Subscriber  

class NewsletterSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(read_only=True)
    recipients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Subscriber.objects.all(),
        required=False,
        default=[]
    )

    class Meta:
        model = Newsletter
        fields = '__all__'

    def create(self, validated_data):
        # Assign the logged-in user automatically
        validated_data['admin'] = self.context['request'].user
        recipients_data = validated_data.pop('recipients', [])
        newsletter = super().create(validated_data)
        newsletter.recipients.set(recipients_data)
        return newsletter

    def update(self, instance, validated_data):
        recipients_data = validated_data.pop('recipients', None)
        newsletter = super().update(instance, validated_data)
        if recipients_data is not None:
            newsletter.recipients.set(recipients_data)
        return newsletter
