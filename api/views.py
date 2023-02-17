from rest_framework import viewsets, permissions, response, status

from .serializers import CaptchaSerializer
from .models import Captcha
 
class CaptchaViewSet(viewsets.ModelViewSet):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
