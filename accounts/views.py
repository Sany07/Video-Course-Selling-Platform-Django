from django.contrib import messages, auth
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views.generic import CreateView, RedirectView, View , ListView, TemplateView, FormView

from courses.models import *
from accounts.forms import *

class InstructorRegisterView(CreateView):
    """
        Provides the ability to Register as a Instructor
    """
    model = CustomUser
    form_class = TeacherRegistrationForm
    template_name = "accounts/instructor-register.html"


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('coresite:home')
        return super().dispatch(self.request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect('accounts:login')
        else:
            context={
                'form':form
            }
            return render(request, self.template_name ,context)

class StudentRegisterView(CreateView):
    """
        Provides the ability to Register as a Student
    """
    model = CustomUser
    form_class = StudentRegistrationForm
    template_name = "accounts/student-register.html"


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('coresite:home')
        return super().dispatch(self.request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect('accounts:login')
        else:
            context={
                'form':form
            }
            return render(request, self.template_name ,context)


class LogInView(FormView):
    """
        Provides the ability to login as a user with an email/username and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))    


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


def create_course_with_lessons(request):
    courseform = CourseModelForm(request.POST or None)
    formset = LessonFormset(queryset=Lesson.objects.none())
    ContentFormset = LessonContentFormset(queryset=LessonContent.objects.none())
    
    if request.method == 'POST':

        courseform = CourseModelForm(request.POST or None , request.FILES or None)
        formset = LessonFormset(request.POST)
        ContentFormset = LessonContentFormset(request.POST)
        
        if courseform.is_valid and formset.is_valid() and ContentFormset.is_valid():
            categories = Category.objects.get(id=1) 
            course  = courseform.save(commit=False)
            # course.category=categories
            course.save()
            
            
            for form in ContentFormset:
                lesson = form.save(commit=False)         
                lesson.save()
            for form in formset:
                author = form.save(commit=False)
                author.course = course
                author.save()
                author.video_link.add(lesson)
                
    categories = Category.objects.all()   
    return render(request, 'courses/create-course.html', {
        'courseform': courseform,
        'formset': formset,
        'ContentFormset':ContentFormset,
        'categories':categories

    })



