from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ["id", "phone_number", "admin", "created_at"]
        read_only_fields = ["admin", "created_at"]

    def create(self, validated_data):
        # Automatically assign the logged-in admin
        validated_data["admin"] = self.context["request"].user
        return super().create(validated_data)
