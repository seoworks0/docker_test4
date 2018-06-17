from django.http import JsonResponse
from django.views import generic
from .models import Post
from .suggest import main

class PostList(generic.ListView):
    model = Post


def api_v2_posts(request):

    # 新規作成
    if request.method == 'POST':
        title = request.POST.get('title')
        #main(title)
        #rank="1"
        #r_url = "unko.jp"


        post = Post(title=title)
        post.save()
        d = {
            'pk': post.pk,
            'created_at': post.created_at,
            'title': post.title,
        }

        #query = request.GET.get('query')
        return JsonResponse(d)
