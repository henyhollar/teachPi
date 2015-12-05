from rest_framework import generics, permissions, status, exceptions
from rest_framework.views import APIView
from serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.contrib.auth import authenticate


from django.contrib.auth import get_user_model

User = get_user_model()



class RegisterView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'register.html'

 #    def get(self, request):
	# serializer = RegisterSerializer()
	# return Response({'serializer': serializer})

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# serializer = RegisterSerializer()
	# if not serializer.is_valid():
 #            return Response({'serializer': serializer})
 #        return redirect('attendance')

class LoginView(APIView):

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }
        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return Response({'user': request.user})
        return Response({'user': None})

    def post(self, request, *args, **kwargs):
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'success': True, 'username': username})
            return self._error_response('disabled')
        return self._error_response('invalid')
    

# class IndexView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'

#     def get(self, request, *args, **kwargs):
#         serializer = LoginSerializer()
#         return Response({'serializer': serializer})
