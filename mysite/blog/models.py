from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    # 文章标题
    title = models.CharField('标题', max_length=70)

    # 文章正文
    body = models.TextField('正文')

    # 创建时间
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
