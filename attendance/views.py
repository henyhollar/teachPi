from rest_framework.views import APIView
from rest_framework import permissions
from redis_ds.redis_list import RedisList
#from redis_ds.redis_hash_dict import RedisHashDict
from rest_framework.response import Response
from redis import StrictRedis
from course.models import Course
from .permissions import CanTakeCourse
from .serializers import AttendanceSerializer

from datetime import datetime
from .models import Attendance



class Get_Who_Attended(APIView):
    """
    this class if for the staff to call. It returns the marked attendance with the user information
    the parameters are:
        course_code: string
        date: string
    """

    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, **kwargs):
        attendance = []
        attend = Attendance.objects.filter(course_code=kwargs['course_code'])
        if all([kwargs.has_key('year'), kwargs.has_key('month'), kwargs.has_key('day')]):
            date_str = '{} {} {}'.format(kwargs['year'], kwargs['month'], kwargs['day'])
            date = datetime.date(datetime.strptime(date_str, '%Y %b %d'))
            attend = attend.filter(date=date)
        for att in attend:
            print att
            attendance.append({'first_name': att.user.first_name,
                          'last_name': att.user.last_name,
                          'matric_no': att.user.matric_no,
                          'date': att.date,
                          'time': att.time,
                          'course_code': att.course_code
            })

        return Response(attendance)


class AttendanceView(APIView):
    """
    the parameters are:
        matric_no: string
        status: boolean
        course_code: string
        duration: integer
    """
    permission_classes = (permissions.IsAuthenticated, CanTakeCourse)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            #duration = request.POST.get('duration')
            #equest.session.set_expiry(duration*3600) set the expiry of the token
            return Response({'success': 'Attendance marked!'})

        return Response(serializer.errors)


class ActiveClass(APIView):
    """
    This section will give the class available or return none when called
    Parameters required are:
    course_code: string
    duration: integer
    """

    permission_classes = (permissions.IsAuthenticated,)

    redis_key = 'active_class:'

    def get(self, request):
        r = StrictRedis(host='localhost', port=6379, db=0)
        course_code = r.keys('active_class:*')
        course_code = course_code[0].split(':')[1] if len(course_code) > 0 else ''
        if not course_code:
            return Response('There is no active course!')
        try:
            course = Course.objects.filter(course_code=course_code)
        except Course.DoesNotExist:
            return Response('There is no course listed yet!')
        return Response(course.values())

    def post(self, request):
        course_code = request.POST.get('course_code')
        duration = int(request.POST.get('duration'))

        r = StrictRedis(host='localhost', port=6379, db=0)
        r.set('{}{}'.format(self.redis_key, course_code), course_code)
        r.expire('{}{}'.format(self.redis_key, course_code), duration*3600)

        return Response({'success': 'active_class stored'})









#def get_client_ip(request):
#    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#    if x_forwarded_for:
#        ip = x_forwarded_for.split(',')[-1].strip()
#    else:
#        ip = request.META.get('REMOTE_ADDR')
#    return ip

#or django-ipaware