from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(editable=False)
    tags = models.ManyToManyField('Tag')

    def save(self, *args, **kargs):
        if not self.created_at:
            self.created_at = timezone.now()
        return super().save(*args, **kargs)


    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name