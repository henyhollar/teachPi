from rest_framework.views import APIView
from .models import Course
from redis_ds.redis_list import RedisList
from rest_framework import permissions
from rest_framework.response import Response



class CourseView(APIView):
	"""
	can be edited by staff only. The staff can fill in the details of 
	the courses here. The course_info can contain the name of the 
	lecturer in charge and some other anouncements
	
	Parameter for post:
		course_title: string
		course_code: string
		duration: int
		coure_info: text
		
	Parameter for put
		course_code: string
		course_title: string
		duration: int
		coure_info: text
		
	Parameter for delete
		course_code: string
		
	"""
	permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser) 


	def get(self, request):
		return Response(Course.objects.all().values())

	def post(self, request):
		Course.objects.create(course_title=request.POST.get('course_title'), course_code=request.POST.get('course_code'),
		duration=request.POST.get('duration'), course_info=request.POST.get('course_info')
		)
		return Response({'sucess': 'course registered'})

	def put(self, request):
		Course.objects.filter(course_code=request.data['course_code']).update(course_title=request.data['course_title'], duration=request.data['duration'], 
		course_info=request.data['course_info']
		)
		return Response({'sucess': 'course updated'})
		
	def delete(self, request):
		course = Course.objects.filter(course_code=request.data['course_code']).delete()
		return Response({'sucess': 'course deleted'})
		
		
class CanTakeCourse(APIView):
	"""
	can be edited by staff only. The excel file will be uploaded into 
	the app and the app will extract the matric_no of registered students
	then it will call the API
	
	Parameters
		course_code: string
		can_take_course: a list of matric_nos that registered for the course
	"""
	
	permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser) 

	def get(self, request, **kwargs):
		redis_can_take_course = RedisList(kwargs['course_code'])
		return Response(redis_can_take_course[:])

	def post(self, request):
		
		redis_can_take_course = RedisList(request.data['course_code'])
		for item in request.data['can_take_course']:
			redis_can_take_course.append(item)
			
		return Response({'success':'can_take_course'})
		
	
