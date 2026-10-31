from django.shortcuts import render, redirect, get_object_or_404
from .forms import UniversityForm, StudentForm
from . import models



def university_list(request):
    universities = models.University.objects.all()

    return render(request, 'university/university_list.html', {
        'universities': universities
    })

def university_create(request):
    form = UniversityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('university_list')

    return render(request, 'university/university_form.html', {
        'form': form
    })


def university_update(request, pk):
    university = get_object_or_404(models.University, pk=pk)
    form = UniversityForm(request.POST or None, instance=university)

    if form.is_valid():
        form.save()
        return redirect('university_list')

    return render(request, 'university/university_form.html', {
        'form': form
    })

def university_delete(request, pk):
    university = get_object_or_404(models.University, pk=pk)

    if request.method == 'POST':
        university.delete()
        return redirect('university_list')

    return render(request, 'university/university_confirm_delete.html', {
        'object': university
    })

def student_list(request):
    students = models.Student.objects.select_related('university').all()

    return render(request, 'student/student_list.html', {
        'students': students
    })

def student_create(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'student/student_form.html', {
        'form': form
    })

def student_update(request, pk):
    student = get_object_or_404(models.Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'student/student_form.html', {
        'form': form
    })


def student_delete(request, pk):
    student = get_object_or_404(models.Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student/student_confirm_delete.html', {
        'object': student
    })

