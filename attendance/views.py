from rest_framework.views import APIView

from .models import Attendance


class AttendanceView(APIView):
	"""Note that attendance cannot be called later than 20 mins after the start of class """

	def post(self, request, format=None):
		#get the start time of the course (from the point the staff presses a button for the start) and check with the current time
        return Attendance.objects.create(user=request.user.id, status=request.POST.get('status'), course=request.POST.get('course'))

		

