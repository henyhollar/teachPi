from django.db import models

# Create your models here.

class Course(models.Model):
	course_title = models.TextField()
	course_code = models.CharField(max_length=6, unique=True)
	duration = models.IntegerField()
	course_info = models.TextField(blank=True)

	def __unicode__(self):
		return '{}:{}'.format(course_code, course_title)

	
