from django.contrib.auth import get_user_model
from django.db import models
from django.db import models

# Create your models here.

User = get_user_model()


# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=None)
    text_content = models.TextField()
    audio_content = models.FileField(upload_to='audio', null=True)
    video_content = models.FileField(upload_to='video', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.user}, {self.id}, {self.title}"
