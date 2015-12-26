from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Attendance

User = get_user_model()


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ('course_code',)

    def save(self, **kwargs):
        assert self.instance is None, 'Cannot update users with CreateUserSerializer'
        Attendance.objects.create(user=self.context['request'].user, course=self.validated_data['course_code'].upper())


