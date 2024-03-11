from django.db import models

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