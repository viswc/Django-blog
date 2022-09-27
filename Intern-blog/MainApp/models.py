from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid

class Blog(models.Model):
	dateCreated = models.DateTimeField(auto_now_add = True)
	dateModified = models.DateTimeField(auto_now = True)
	primaryKey = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	title = models.CharField(max_length = 512, default="BlogTitleProvider")
	thumbnail = models.ImageField(upload_to='data/media/primary/', null=True, blank = True)
	readTime = models.CharField(max_length = 32, null=True, blank = True)
	content = RichTextUploadingField(max_length = 100000, null = True, blank = True)