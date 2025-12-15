import requests
from django.conf import settings


class NotifyService:
    """
    Handles all communication with the Notify Africa SMS API
    """

    @staticmethod
    def send_sms(phone_number: str, message: str) -> dict:
        """
        Send an SMS via Notify Africa

        Returns:
            {
              "success": bool,
              "response": dict | str
            }
        """

        url = f"{settings.NOTIFY_BASE_URL}/messages/send"

        headers = {
            "Authorization": f"Bearer {settings.NOTIFY_API_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "phone_number": phone_number,      
            "message": message,
            "sender_id": settings.NOTIFY_SENDER_ID,
        }

        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=10,
            )

            if response.status_code == 200:
                return {
                    "success": True,
                    "response": response.json(),
                }

            return {
                "success": False,
                "response": response.text,
            }

        except requests.RequestException as e:
            return {
                "success": False,
                "response": str(e),
            }
