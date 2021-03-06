import django
from django.db import models
from django.utils import timezone
# Create your models here.

class Tool(models.Model):
    name = models.CharField(blank=True, max_length=20, verbose_name="툴이름")
    type = models.CharField(blank=True, max_length=20, verbose_name="툴종류")
    content = models.TextField(blank=True, verbose_name="툴설명")

class Post(models.Model):
    title = models.CharField(blank=True,verbose_name ="제목", max_length=50)
    image = models.ImageField(blank=True, verbose_name ="이미지", upload_to='posts/%Y%m%d', height_field=None, width_field=None, max_length=None)
    content = models.TextField(blank=True,verbose_name ="내용")
    interest = models.CharField(blank=True,verbose_name ="관심도", max_length=50)
    devtool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="post_tool", blank=True)    
    created_at = models.DateTimeField(blank=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,auto_now=True)

# class IdeaStar(models.Model):
#     post = models.ManyToManyField(
#         "post.Post",
#         related_name="list",
#         blank=True,
#     )
#     def count_posts(self):
#         return self.post.count()