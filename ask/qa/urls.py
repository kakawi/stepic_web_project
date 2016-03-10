from django.conf.urls import patterns, include, url
from qa.views import test
from qa.views import homepage
from qa.views import popular
from qa.views import question

urlpatterns = patterns('qa.views',
    url(r'^$', homepage, name='homepage'),
    url(r'^popular/$', popular, name='popular'),
    url(r'^question/(?P<id>\d+)/$', question, name='question_id'),

    url(r'^login/$', test, name='login'),
    url(r'^signup/$', test, name='signup'),

    url(r'^ask/$', test, name='ask'),
    url(r'^ask//popular/$', test, name='popular'),
    url(r'^new/$', test, name='new'),
)
