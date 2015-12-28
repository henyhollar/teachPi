from rest_framework.views import APIView
from rest_framework import permissions
from redis_ds.redis_list import RedisList
#from redis_ds.redis_hash_dict import RedisHashDict
from rest_framework.response import Response
from redis import StrictRedis
from course.models import Course
from .permissions import CanTakeCourse
from .serializers import AttendanceSerializer

from django.db.models import Q

from .models import Attendance



class Get_Who_Attended(APIView):
    '''
    this class if for the staff to call. It returns the marked attendance
    with the user and matric_no
    '''
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, **kwargs):
        attend = Attendance.objects.filter(course_code=kwargs['course_code']).select_related('user')
        attendance = {'username': attend[0].user.username,
                      'matric_no': attend[0].user.matric_no,
                      'date': attend[0].date,
                      'time': attend[0].time,
                      'course_code': attend[0].course_code
        }

        return Response(attendance)


class AttendanceView(APIView):	
    '''
    the parameters are:
        matric_no: string
        status: boolean
        course_code: string
        duration: integer
    '''

    permission_classes = (permissions.IsAuthenticated, CanTakeCourse)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

        #duration = request.POST.get('duration')
        #equest.session.set_expiry(duration*3600) set the expiry of the token

        return Response({'success': 'Attendance marked!'})


class ActiveClass(APIView):
	"""
	This section will give the class available or return none when called
	Parameters required are:
		course_code: string
		duration: integer
	"""

	permission_classes = (permissions.IsAuthenticated,)

	redis_key = 'active_class'

	def get(self, request):
		r = StrictRedis(host='localhost', port=6379, db=0)
		course_code = r.get(self.redis_key)
		if not course_code:
			return Response('There is no active course!')
		try:
			course = Course.objects.filter(course_code=course_code)
		except Course.DoesNotExist:
			return Response('There is no course listed yet!')

		return Response(course.values())

	def post(self, request):
		active_class = request.POST.get('course_code')
		duration = int(request.POST.get('duration'))
		print active_class, duration

		r = StrictRedis(host='localhost', port=6379, db=0)
		r.set(self.redis_key, active_class)
		r.expire(self.redis_key, duration*3600)

		return Response({'success':'active_class stored'})









