from rest_framework import serializers

from .models import Captcha

class CaptchaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Captcha
        fields = ('title', 'image')