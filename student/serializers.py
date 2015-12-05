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

	def validate_username(self, value):
		try:
			user = User.objects.get(username=value)
			raise serializers.ValidationError('Username already exists please choose another')
		except User.DoesNotExist:
			return value
			
	def validate_email(self, value):
		try:
			user = User.objects.get(email=value)
			raise serializers.ValidationError('Email already exists please choose another')
		except User.DoesNotExist:
			return value
		
			
			
	def validate_matric_no(self, value):
		matric_no = value.upper()
		
		if any([all([matric_no.startswith('EEG'),len(value) == 12]), 
			all([matric_no.startswith('TP'),len(value) == 14]),
			all([matric_no.startswith('AC'),len(value) == 8])]):
			try:
				user = User.objects.get(matric_no=value)
				raise serializers.ValidationError('Matric No. already exists please report if someone else has used yours')
			except User.DoesNotExist:
				return value
		else:
			raise serializers.ValidationError('Matric No. is not valid')

			

	#def validate(self, data):
		#if data['password'] == data['confirm_password']:
			#return data
		#else:
			#raise serializers.ValidationError('The passwords entered are not the same')


	def save(self):
		user = User.objects.create_user(self.validated_data['username'], self.validated_data['email'], self.validated_data['password'])
		user.first_name = self.validated_data['first_name']
		user.last_name = self.validated_data['last_name']
		user.matric_no = self.validated_data['matric_no']

		user.save()
