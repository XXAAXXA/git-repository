from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])