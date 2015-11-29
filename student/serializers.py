from rest_framework import serializers
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    matric_no = serializers.CharField(
        max_length=20,
        style={'placeholder': 'Matric No.'}
    )

    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    remember_me = serializers.BooleanField()


class RegisterSerializer(serializers.Serializer):
	matric_no = serializers.CharField(
		max_length = 20,
		style = {'placeholder': 'Matric No.', 'class': 'textbox'}
	)

	surname = serializers.CharField(
		max_length = 50,
		style = {'placeholder': 'Surname', 'class': 'textbox'}
	)

	first_name = serializers.CharField(
                max_length = 50,
                style = {'placeholder': 'First name', 'class': 'textbox'}
        )

	password = serializers.CharField(
                max_length = 100,
                style = {'input-type': 'password', 'placeholder': 'Password' }
	)

	confirm_password = serializers.CharField(
                max_length = 100,
                style = {'input-type': 'password', 'placeholder': 'Password'}
        )


