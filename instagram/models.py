from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/user',null=True,blank=True)

@receiver(post_save, sender=User)
def handler(sender,instance,created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance).save()
    


class Post(models.Model):
    picture  = models.ImageField(upload_to='images/posts')
    post_body = models.TextField(verbose_name='Post Body')
    likes = models.PositiveBigIntegerField(default=0)
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
