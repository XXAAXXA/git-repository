from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm


@require_POST
def comment(request, post_pk):
    # 先获取被评论的文章
    post = get_object_or_404(Post, pk=post_pk)

    # django 将用户提交的数据封装在 request.POST 中
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        # 将评论和被评论的文章关联
        comment.post = post

        # 将评论数据保存进数据库
        comment.save()

        return redirect(post)

    # 检查到数据不合法，我们渲染一个预览页面，用于展示表单的错误。
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'comments/preview.html', context=context)