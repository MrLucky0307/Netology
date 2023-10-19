from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    template = 'school/student_list.html'
    model = Student
    ordering = 'group'
    queryset = Student.objects.all().prefetch_related('teacher')
