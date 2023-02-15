from django.db import models

class Captcha():
    image = models.ImageField()
    title = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.title