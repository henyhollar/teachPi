from rest_framework import generics, permissions, status, exceptions
from rest_framework.views import APIView
from serializers import LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect


from django.contrib.auth.models import User


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self, request):
	serializer = RegisterSerializer()
	return Response({'serializer': serializer})

    def post(self, request):
	serializer = RegisterSerializer()
	if not serializer.is_valid():
            return Response({'serializer': serializer})
        return redirect('attendance')

class LoginView(APIView):
	pass
