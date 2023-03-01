from rest_framework import serializers

from .models import Captcha

class CaptchaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Captcha
        fields = ['id', 'image']
        read_only_fields = ['id', 'image']