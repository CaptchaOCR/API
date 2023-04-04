from django.db import models

class Captcha(models.Model):

    title = models.CharField(max_length=5, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.title
