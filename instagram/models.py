from django.db import models


class Post(models.Model):
    post_body = models.TextField(verbose_name='Post Body')
    created_time = models.DateTimeField(verbose_name='Created Time')

    def __str__(self):
        return f"{self.id}__{self.post_body}"
    

class Comment(models.Model):
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}__{self.body}"