from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Teacher
from .models import visitors
from .models import Post

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(visitors)
admin.site.register(Post)
