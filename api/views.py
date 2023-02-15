from rest_framework import viewsets

from .serializers import CaptchaSerializer
from .models import Captcha
 
class CaptchaViewSet(viewsets.ModelViewSet):
    queryset = Captcha.objects.all()
    serializer_class = CaptchaSerializer