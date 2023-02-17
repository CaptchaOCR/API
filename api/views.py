from rest_framework import viewsets, permissions

from .serializers import CaptchaSerializer
from .models import Captcha
 
class CaptchaViewSet(viewsets.ModelViewSet):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaSerializer
    permission_classes = [permissions.IsAuthenticated]

'''
    def create(self, request ):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        Captcha.objects.create().save()
'''