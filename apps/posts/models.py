from django.db import models


class StatusChoices(models.TextChoices):
    AVAILABLE = ('available',)
    UNAVAILABLE = ('unavailable',)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField()
    status = models.CharField(max_length=30, choices=StatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
