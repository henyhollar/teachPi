from rest_framework.views import APIView
from redis_ds.redis_list import RedisList
#from redis_ds.redis_hash_dict import RedisHashDict
from rest_framework.response import Response
from redis import StrictRedis
from course.models import Course


from .models import Attendance


class AttendanceView(APIView):	
	def get(self, request, format=None):
		attend = Attendance.objects.all().select_related('username', 'matric_no')
		return Response(attend.values())
		
	def post(self, request, format=None):
		duration = request.POST.get('duration')
		request.session.set_expiry(duration*3600)
		Attendance.objects.create(user=request.user.id, status=request.POST.get('status'), course=request.POST.get('course'))
		return Response({'success': 'attendance'})
	    
	        
class ActiveClass(APIView):
	""" This section will give the class availble or return none when called"""
	redis_key = 'active_class'
	
	def get(self, request):		
		r = StrictRedis(host='localhost', port=6379, db=0)
		course_code = r.get(self.redis_key)
		if not course_code:
			return Response('There is no active course!')
		try:
			course = Course.objects.get(course_code=course_code)
		except Course.DoesNotExist:
			return Response('There is no course listed yet!')
		
		return Response(course.values())
		
	def post(self, request):
		active_class = request.POST.get('course_code')
		duration = int(request.POST.get('duration'))
		
		r = StrictRedis(host='localhost', port=6379, db=0)
		r.set(self.redis_key, active_class)
		r.expire(self.redis_key, duration*3600)
		
		return Response({'success':'active_class'})
		
		
	 

	 
		

