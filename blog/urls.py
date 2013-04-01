from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'blog.views.front'),
    (r'newpost/', 'blog.views.main'),  
)
