from rest_framework.views import APIView
from redis_ds.redis_list import RedisList
#from redis_ds.redis_hash_dict import RedisHashDict
from rest_framework.response import Response
from redis import StrictRedis


from .models import Attendance


class AttendanceView(APIView):
	"""Note that attendance cannot be called later than 20 mins after the start of class """
	
	def get(self, request, format=None):
		attend = Attendance.objects.all().select_related()
		return Response(attend.values())
		
	def post(self, request, format=None):
		#get the start time of the course (from the point the staff presses a button for the start) and check with the current time
	        return Attendance.objects.create(user=request.user.id, status=request.POST.get('status'), course=request.POST.get('course'))
	        
	        
class ActiveClass(APIView):
	""" This section will give the class availble or return none when called"""
	redis_key = 'active_class'
	
	def get(self, request):
		r = StrictRedis(host='localhost', port=6379, db=0)
		active_class = r.get(self.redis_key, active_class)
		
		return Response(active_class)
		
	def post(self, request):
		active_class = request.POST.get('course_code')
		duration = int(request.POST.get('duration'))
		
		r = StrictRedis(host='localhost', port=6379, db=0)
		r.set(self.redis_key, active_class)
		r.expire(self.redis_key, duration*3600)
		
		return Response()
		
		
	 

	 
		

