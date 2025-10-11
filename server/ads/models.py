from django.db import models
from django.conf import settings


class Campaign(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ad_campaigns')
    name = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Ad(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='ads')
    media = models.FileField(upload_to='ads/')
    target_url = models.URLField()
    impressions = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
