from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ["id", "phone_number", "owner", "created_at"]
        read_only_fields = ["owner", "created_at"]

    def create(self, validated_data):
        # Automatically assign the logged-in owner
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
