from rest_framework.views import APIView
from .models import Course

class CourseView(APIView):

	def get(self, request):
		return Course.objects.all()

	def post(self, request):
		return Course.objects.create(course_title=request.POST.get('course_title'), course_code=request.POST.get('course_code'),
		 duration=request.POST.get('duration'), course_info=request.POST.get('course_info')
		 )

	def put(self, request):
		pass