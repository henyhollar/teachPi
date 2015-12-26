from django.conf.urls import url

from .import views


urlpatterns = [
	url(r'^$', views.AttendanceView.as_view(), name='attendance'),
	url(r'^activeclass/$', views.ActiveClass.as_view(), name='active_class_get'),
	url(r'^attendance_list/(?P<course_code>[A-Z0-9]{6})/$', views.Get_Who_Attended.as_view(), name='get_who_attended'),
]
