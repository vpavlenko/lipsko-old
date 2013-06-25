from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'main_web.views.home', name='home'),
)
