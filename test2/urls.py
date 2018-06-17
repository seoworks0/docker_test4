from django.conf.urls import url
from django.contrib import admin
from .views import PostList, api_v2_posts
from django.urls import path, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostList.as_view(), name='post_list2'),
    url(r'^api/v2/posts$', api_v2_posts, name='api_v2_posts'),
]
