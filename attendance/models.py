from django.db import models
from django.conf import settings

# Create your models here.

class Attendance(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user')
	#status = models.BooleanField(default=False)
	course_code = models.CharField(max_length=300)
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	
	 
	class Meta:
		unique_together = ('user','course_code', 'date',)
	
	def __unicode__(self):
		return "{}:{}:{}".format(self.user, self.course_code)
