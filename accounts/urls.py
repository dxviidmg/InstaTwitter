from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [


	url(r'^logout/$', logout, name="logout"),
	url(r'^users/$', views.listview, name="user_list"),
	url(r'^profile/$', views.profileview, name="profile"),
	url(r'^user/(?P<username>[-\w]+)/$', views.detailview, name="user_detail"),
	url(r'^follow/$', views.user_follow, name="user_follow"),
	url(r'^', login, name="login"),
]