from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .serializers import CaptchaSerializer
from .models import Captcha
from .func import run_model

import os
 
class CaptchaViewSet(viewsets.ModelViewSet):
    queryset = Captcha.objects.get_queryset().order_by('id')
    serializer_class = CaptchaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        
        response = Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

        result = run_model()

        response.data['code'] = result[0]
        response.data['info'] = result[1]

        print(response.data['image'])
        Captcha.objects.filter(id=response.data['id']).delete()

        return response
