from .utils import generic_search
from attendance.models import Attendance
from rest_framework.response import Response


MODEL_MAP = { Attendance: ["first_name","last_name",],
			 Book  : ["title", "summary"],

}

def search(request, *args):


   objects = []

   for model,fields in MODEL_MAP.iteritems():

	   objects+=generic_search(request,model,fields,args)

   return Response('')

