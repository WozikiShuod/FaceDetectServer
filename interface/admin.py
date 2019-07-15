from django.contrib import admin
from .models import Teacher,Student,Course,Train
from django.utils.html import format_html

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id','stu_name','stu_class')
    list_filter = ('stu_class',)


class TeacherAdmin(admin.ModelAdmin):
    list_display= ('teacher_id','teacher_name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('stu_info','stu_sign_status','stu_sign_time','course','teacher_info','classroom')
    list_filter = ('course','classroom','teacher_info')


class TrainAdmin(admin.ModelAdmin):
    list_display = ('tran_stu_id', 'operator')

    def operator(self, obj):
        return format_html(
            '<a href="{}">训练</a>',
            obj.tran_stu_id
        )
    operator.short_description = '操作'


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Train,TrainAdmin)
