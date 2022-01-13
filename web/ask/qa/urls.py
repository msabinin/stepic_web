from django.conf.urls import url, include
from qa import views

urlpatterns = [
               url(r'(?P<pk>\d+)/', views.test, name='test'),
]
