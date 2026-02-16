from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author_name = models.CharField(max_length=64)
    likes_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    
class Comment(models.Model):
    post_title = models.CharField(max_length=120)  
    author_name = models.CharField(max_length=64)
    text = models.TextField()
    likes_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.post_title}"

