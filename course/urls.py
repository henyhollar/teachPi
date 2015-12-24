from django.conf.urls import url

from .import views


urlpatterns = [
	url(r'^$', views.CourseView.as_view(), name='post_course'),
	url(r'^(?P<course_code>[A-Z0-9]{6})/$', views.CourseView.as_view(), name='get_course'),
	url(r'^can_take_course/$', views.CanTakeCourse.as_view(), name='can_take_course'),
]
