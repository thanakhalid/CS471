from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create your models here.

    
class Poems(models.Model):
    poem_id = models.IntegerField(primary_key = True)
    poem_link = models.URLField(max_length = 255)
    poem_style = models.CharField(max_length = 255)
    poem_text = models.TextField()
    poem_title = models.CharField(max_length = 255)
    poet_cat = models.CharField(max_length = 255)
    poet_id = models.CharField(max_length = 255)
    poet_link = models.URLField(max_length = 255)
    poet_name = models.CharField(max_length = 255)


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    poem = models.ForeignKey(Poems, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.poem.poem_title}"