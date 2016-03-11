from django.conf.urls import patterns, include, url
from qa.views import test
from qa.views import homepage
from qa.views import popular
from qa.views import question
from qa.views import ask_form

urlpatterns = patterns('qa.views',
    url(r'^$', homepage, name='homepage'),
    url(r'^popular/$', popular, name='popular'),
    url(r'^question/(?P<id>\d+)/$', question, name='question_id'),

    url(r'^login/$', test, name='login'),
    url(r'^signup/$', test, name='signup'),

    url(r'^ask/$', ask_form, name='ask'),
    url(r'^ask//popular/$', test, name='popular'),
    url(r'^new/$', test, name='new'),
)
