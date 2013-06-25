from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url(r'^$', 'main_web.views.home.home', name='home'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
