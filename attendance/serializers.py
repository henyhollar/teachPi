from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Attendance

User = get_user_model()


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ('course_code',)

    def validate(self, attrs):
        field1 = attrs.get('field1', self.object.field1)
        field2 = attrs.get('field2', self.object.field2)

        try:
            obj = Model.objects.get(field1=field1, field2=field2)
        except StateWithholdingForm.DoesNotExist:
            return attrs
        if self.object and obj.id == self.object.id:
            return attrs
        else:
            raise serializers.ValidationError('field1 with field2 already exists')

    def save(self, **kwargs):
        assert self.instance is None, 'Cannot update users with CreateUserSerializer'
        Attendance.objects.create(user=self.context['request'].user, course_code=self.validated_data['course_code'].upper())


