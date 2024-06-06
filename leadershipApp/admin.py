from django.contrib import admin

from .forms import CeoForm
from .models import CustomUser,StudentRecord,Ceo,Message,About,Course 

admin.site.register(CustomUser)
admin.site.register(StudentRecord)
admin.site.register(Ceo)
admin.site.register(Message)
admin.site.register(About)
admin.site.register(Course)