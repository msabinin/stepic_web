from django.conf.urls import url, include
from qa import views
from ask.views import return_ok

urlpatterns = [
               url(r'^$', views.new_posts, name='new'),
               url(r'^login/', views.userLogin, name='login'),
               url(r'^signup/', views.userSignUp, name='signup'),
               url(r'^logout/', return_ok, name='logout'),
               url(r'^ask/', views.ask, name='ask'),
               url(r'^popular/', views.popular_posts, name='popular'),
               url(r'^new/', return_ok, name='ok'),
               url(r'^question/(?P<pk>\d+)/', views.post_details, name='details'),
              ]
