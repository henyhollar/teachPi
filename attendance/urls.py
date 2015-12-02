from django.conf.urls import url

from .import views


urlpatterns = [
	url(r'^$', views.AttendanceView.as_view(), name='attendance'),
]
