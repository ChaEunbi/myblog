from django.conf.urls import url
from blog.views import *

urlpatterns = [
        #Example: /
        url(r'^$', PostLV.as_view(), name='index'),

        #Example: /post/
        url(r'^post/$', PostLV.as_view(), name='post_list'),

        #Example: /archive/
        #url(r'^archive/$', PostAV.as_view(), name='post_archive'),

        #Example: /post/django-example/
        url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

        #Example: /add/
        url(r'^add/$', PostCreateView.as_view(), name="add",),
]
