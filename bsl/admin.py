from django.contrib import admin
from .models import Question,user,Attempt,Stats
# Register your models here.

admin.site.register(Question)
admin.site.register(user)
admin.site.register(Attempt)
admin.site.register(Stats)
