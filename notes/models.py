from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, default=None)
    text_content = models.TextField()
    audio_content = models.FileField(upload_to='audio', null=True)
    video_content = models.FileField(upload_to='video', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.id}, {self.title}"
