from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    price = models.IntegerField(verbose_name = "상품가격", null=True)
    stock = models.IntegerField(verbose_name = "상품재고", null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to= 'images/', null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)


class Comment(models.Model):
    content = models.TextField()
    grade = models.IntegerField(verbose_name="평점", null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comment')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
