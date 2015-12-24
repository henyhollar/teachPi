from django.conf.urls import url

from .import views

"""
To login, the client will call /student/login/. This will return
the token in the response content. The client will build:
		{"Authorization": "Token 93442......."} 
and add it to the header of all subsequent requests.
	
"""

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^userDetails/$', views.UserDetails.as_view()),
    url(r'^login/$', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^logout/$', views.DeleteToken.as_view()),
    url(r'^changePasswords/(?P<username>[0-9]{11})/$', views.ChangePassword.as_view()),
]


