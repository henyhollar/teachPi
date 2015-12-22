from django.conf.urls import url

from .import views


urlpatterns = [
	url(r'^$', views.CourseView.as_view(), name='course'),
	url(r'^can_take_course/$', views.CanTakeCourse.as_view(), name='can_take_course'),
]
