from django.contrib import admin

from .models import Question
# allows admin to add Question
admin.site.register(Question)