from django.conf.urls import url, include
from qa import views
from ask.views import return_ok

urlpatterns = [
               url(r'^$', views.new_posts, name='new_posts'),
               url(r'^login/', return_ok, name='ok'),
               url(r'^signup/', return_ok, name='ok'),
               url(r'^ask/', return_ok, name='ok'),
               url(r'^popular/', return_ok, name='ok'),
               url(r'^new/', return_ok, name='ok'),
               url(r'^question/(?P<pk>\d+)/', views.test, name='test'),
              ]
