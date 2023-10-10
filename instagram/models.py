from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    age = models.PositiveSmallIntegerField()
    Email = models.EmailField(max_length=255 ,unique=True)
    password = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    post_body = models.TextField(verbose_name='Post Body')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='Created Time')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}__{self.post_body[:30]}"
    

class Comment(models.Model):
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Created Time")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}__{self.body[:30]}"
