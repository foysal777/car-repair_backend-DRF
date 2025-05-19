from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'course_applied', 
        'father_name', 
        'date_of_birth', 
        'religion', 
        'nationality',
        'mobile_number', 
        'email'
    )
    search_fields = ('name', 'father_name', 'email', 'mobile_number')
    list_filter = ('religion', 'nationality', 'course_applied')
    ordering = ('-id',)  # latest entries first

admin.site.register(Student, StudentAdmin)
