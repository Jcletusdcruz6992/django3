from django.conf.urls import url
from AppTwo import views
from django.urls import path
urlpatterns=[
url(r'^$',views.index,name='index')
]
