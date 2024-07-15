from django.db import models

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ("video", "Video"),
        ("pdf", "PDF"),
        ("platform", "Platform"),
    ]

    content_name = models.CharField(max_length=100)
    description = models.TextField()
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    content_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.content_name