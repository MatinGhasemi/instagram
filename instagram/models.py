from django.db import models


class Post(models.Model):
    post_body = models.TextField(verbose_name='Post Body')
    created_time = models.DateTimeField(verbose_name='Created Time')

    def __str__(self):
        return self.post_body