from django.db import models

# Create your models here.

class Attendance(models.Model):
	present = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return "{}:{}".format(self.present, self.time)
