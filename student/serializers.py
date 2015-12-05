from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()#(?P<>[a-z0-9]{81,14,12})

#def check_matric_no(matric_no):
	#if matric_no.startswith('EEG') and len(value) == 12:
		#return value
	#elif matric_no.startswith('TP') and len(value) == 14:
		#return value
	#elif matric_no.startswith('AC') and len(value) == 8:
		#return value

	#else:
		#raise serializers.ValidationError('Please check the matric_no')



class RegisterSerializer(serializers.Serializer):
	username = serializers.CharField(
		max_length = 30,
		style = {'placeholder': 'Username'}
	)

	matric_no = serializers.CharField(
        max_length = 14,
        style = {'placeholder': 'Matric No.'}
    )

	last_name = serializers.CharField(
		max_length = 30,
		style = {'placeholder': 'Last name'}
	)

	first_name = serializers.CharField(
		max_length = 30,
        style = {'placeholder': 'First name'}
    )

	email = serializers.EmailField(
		style = {'placeholder': 'Email'}
    )

	password = serializers.CharField(
	    max_length = 30,
        style = {'input-type': 'password', 'placeholder': 'Password' }
	)

	#confirm_password = serializers.CharField(
        #max_length = 30,
        #style = {'input-type': 'password', 'placeholder': 'Confirm Password'}
    #)

	
    
	def validate_email(self, value):
		try:
			user = User.objects.get(email=value)
			if user.username == self.instance.username:
				return value
			else:
				raise serializers.ValidationError('Email already exists please choose another')
		except User.DoesNotExist:
			return value
		#except MultipleObjectsReturned:
            ##if value != u'':
			#raise serializers.ValidationError('Please enter an email address')
			
			
	#def validate_matric_no(self, value):
		#matric_no = value.upper()
        #try:
            #user = User.objects.get(matric_no=matric_no)
        #except User.DoesNotExist:
			##check_matric_no(matric_no)
			#return val

        #raise serializers.ValidationError('Please check the matric_no')


	#def validate(self, data):
		#if data['password'] == data['confirm_password']:
			#return data
		#else:
			#raise serializers.ValidationError('The passwords entered are not the same')


	def save(self):
		user = User(**self.validated_data)
		user.save()
