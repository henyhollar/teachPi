from rest_framework import generics, permissions, status, exceptions
from rest_framework.views import APIView
from serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth import get_user_model


User = get_user_model()



class RegisterView(APIView):
	
    """
    Parameters are:
		username: string
		password: string
		email: string
		matric_no: string
		first_name: string
		last_name: string
    """

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            user = User.objects.get(username=self.request.data['username'])
            
            Token.objects.create(user=user)
			
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   	
class UserDetails(APIView):
	
	permission_classes = (permissions.IsAuthenticated,)

	def get (self, request):
		user = User.objects.filter(username=request.user.username)
		return Response(user.values()[0])
		
	
class ChangePassword(APIView):
	"""
	call this with REST PUT method
	Parameters:
		old_password: string
		new_password: string
	"""
	permission_classes = (permissions.IsAuthenticated,)
	
	def put(self, request, *args, **kwargs):
		user = User.objects.get(username=request.user.username)
		if check_password(request.data['old_password'], user.password):
			user.set_password(request.data['new_password'])
			user.save()
        
			return Response('Password changed successful')
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
class DeleteToken(APIView):
	"""
	Call the logout with the REST delete method
	"""
	def delete(self, request, *args, **kwargs):
		user = User.objects.get(username=request.user.username)
		token = Token.objects.get(user=user)
		logout(request)
		token.delete()
		token.save()
		return Response('Sign-out successful')
	

class DeleteAllToken(APIView):
	'''
	this should be called after the teacher logout.
	'''
	permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser) 

	def delete(self, request, *args, **kwargs):
		token = Token.objects.all()
		#logout(request)
		token.delete()
		token.save()
		return Response('Sign-out successful')
