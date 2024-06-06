from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .forms import AboutForm, CeoForm, CourseForm, CustomUserForm, MessageForm, StudentRecordForm
from .models import About, StudentRecord, Ceo , CustomUser , Message, Course
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator




def adminCourse(request):
    courses = Course.objects.all()
    profile = request.user

    paginator = Paginator(courses, 6)  # Show 6 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'AdminCourse.html', {'page_obj': page_obj, 'profile': profile})



def about(request):
    abouts = About.objects.all()
    profile = request.user
    return render(request, 'About.html', {'abouts':abouts, "profile":profile})


def home(request):
    abouts = About.objects.all()
    dashboards = Ceo.objects.all()
    return render(request,'index1.html', {'abouts':abouts, 'dashboards':dashboards})


def course(request):
    courses = Course.objects.all()
    return render(request,'course.html', {'courses':courses})


def form(request):
    return render(request,'form.html')


@login_required
def dashboard(request):
    # Retrieve all StudentRecord objects
    students = StudentRecord.objects.all()

    # Create a dictionary from StudentRecord objects
    data = {record.month: record.value for record in students}

    # Serialize the data to a JSON string
    json_data = json.dumps(data, cls=DjangoJSONEncoder)

    # Retrieve all Ceo objects
    dashboards = Ceo.objects.all()
    
    profile = request.user
    
    
    # Pass the serialized data and dashboards to the template
    return render(request, 'index.html', {'dashboards': dashboards, 'data': json_data, 'profile':profile})





def profile(request):
    profiles = CustomUser.objects.all()
    profile = request.user
    return render(request, 'pages-profile.html', {'profiles':profiles, "profile":profile})


def message(request):
    messages = Message.objects.all()
    profile = request.user
    
    paginator = Paginator(messages, 10)  # Show 10 messages per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'table-message.html', {'page_obj': page_obj, 'profile': profile})



def student(request):
    students = StudentRecord.objects.all()
    profile = request.user
    
    paginator = Paginator(students, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'student.html', {'page_obj': page_obj, 'profile': profile})




def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        phone = request.POST.get('phone', '')
        image = request.FILES.get('image')  # Get the uploaded image file

        # Check if the email already exists in the database
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'This email is already in use.')
            return render(request, 'register.html')

        try:
            user = CustomUser.objects.create_user(email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.image = image  # Assign the uploaded image to the user's image field
            user.save()
            messages.success(request, 'Your account has been created successfully')
            return redirect('home')  # Replace 'home' with the URL name where you want to redirect after registration
        except Exception as e:
            messages.error(request, f'An error occurred while creating your account: {e}')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def service(request): 
    courses = Course.objects.all()
    return render(request, 'pages-service.html', {'courses':courses})
    
    
    

def SignUP(request):
    if request.method == "POST":
        # Get data from the form
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        month = request.POST.get('month')
        email = request.POST.get('email')
        course = request.POST.get('course')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        current_program = request.POST.get('current_program')
        academic_performance = request.POST.get('academic_performance')
        area_of_specializations = request.POST.get('area_of_specializations')
        leadership_positions_held = request.POST.get('leadership_positions_held')
        duration_of_leadership_roles = request.POST.get('duration_of_leadership_roles')
        leadership_achievements_and_responsibilities = request.POST.get('leadership_achievements_and_responsibilities')
        year_of_study = request.POST.get('year_of_study')
        age = request.POST.get('age')
        value = request.POST.get('value')
        state = request.POST.get('state')
        country = request.POST.get('country')
        image = request.FILES.get('image')
        resume_cv_upload = request.FILES.get('resumeupload')
        file_uploads = request.FILES.get('fileupload')

        # Check if the email already exists
        if StudentRecord.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('sign_up')  # You may want to customize the redirect URL

        try:
            # Create a new StudentRecord instance and save it
            student_record = StudentRecord(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                gender=gender,
                month=month,
                email=email,
                course=course,
                phone_number=phone_number,
                address=address,
                current_program=current_program,
                academic_performance=academic_performance,
                area_of_specializations=area_of_specializations,
                leadership_positions_held=leadership_positions_held,
                duration_of_leadership_roles=duration_of_leadership_roles,
                leadership_achievements_and_responsibilities=leadership_achievements_and_responsibilities,
                year_of_study=year_of_study,
                age=age,
                value=value,
                state=state,
                country=country,
                image=image,
                resume_cv_upload=resume_cv_upload,
                file_uploads= file_uploads
                
            )
            student_record.save()
            messages.success(request, 'Thank you for Signing Up')
            return redirect('sign_up')  # You may want to customize the redirect URL for success
        except Exception as e:
            messages.error(request, f'An error occurred while Signing Up: {str(e)}')
            return redirect('home')  # You may want to customize the redirect URL for error
    return render(request, 'form.html')




def send(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Check if the email already exists
        if StudentRecord.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('home')  # You may want to customize the redirect URL

        try:
            # Create a new StudentRecord instance and save it
            student_record = StudentRecord(
               name=name,
               email=email,
               subject=subject,
               message=message
            )
            student_record.save()
            messages.success(request, 'Thank you for Signing Up')
            return redirect('home')  # You may want to customize the redirect URL for success
        except Exception as e:
            messages.error(request, f'An error occurred while Signing Up: {str(e)}')
            return redirect('home')  # You may want to customize the redirect URL for error
    return render(request, 'index1.html')



def search_courses(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
        courses = Course.objects.filter(course_name__icontains=query)  # Perform a case-insensitive search

        context = {
            'courses': courses,
            'query': query,
        }
        return render(request, 'course.html', context)



# def deletescholarship(request,id):
#     deleteS = Scholarship.objects.get(id=id)
#     deleteS.delete()
#     return redirect('back')





def editAbout(request, id=None):
    if id:
        ceo = Ceo.objects.get(id=id)
    else:
        ceo = None
    
    if request.method == 'POST':
        form = CeoForm(request.POST, request.FILES, instance=ceo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'adm' with the appropriate URL name
    else:
        form = CeoForm(instance=ceo)
        
    return render(request, 'editCeo.html', {'form': form, 'ceo': ceo})




def edit_custom_user(request, id=None):
    user = CustomUser.objects.get(id=id) if id else None

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'editUser.html', {'form': form, 'user': user})


def delete_custom_user(request, id=None):
    if id:
        user = get_object_or_404(CustomUser, id=id)
        user.delete()
        return redirect('profile')  # Redirect after deletion
    else:
        # Handle the case where no ID is provided (optional)
        return HttpResponse("No user ID provided", status=400)
    
    
    
def delete_message(request, id=None):
    if id:
        message = get_object_or_404(Message, id=id)
        print(message)
        message.delete()
        return redirect('message')  # Redirect after deletion
    else:
        # Handle the case where no ID is provided (optional)
        return HttpResponse("No message ID provided", status=400)
    
    
def view_message(request, id=None):
    message = get_object_or_404(Message, id=id)
    form = MessageForm(instance=message)
    return render(request, 'viewMessage.html', {'message':message, 'form':form})



def edit_student_record(request, id=None):
    student = StudentRecord.objects.get(id=id) if id else None
    if request.method == "POST":
        form = StudentRecordForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')  # Replace with your success URL
    else:
        form = StudentRecordForm(instance=student)
    return render(request, 'editStudent.html', {'form': form})


    
def view_student_record(request, id=None):
    student = get_object_or_404(StudentRecord, id=id)
    form = StudentRecordForm(instance=student)
    return render(request, 'viewStudent.html', {'student':student, 'form':form})



def delete_student_record(request, id=None):
    if id:
        student = get_object_or_404(StudentRecord, id=id)
        student.delete()
        return redirect('student')  # Redirect after deletion
    else:
        # Handle the case where no ID is provided (optional)
        return HttpResponse("No student ID provided", status=400)
    
    



def edit_about(request, id=None):
    about_instance = get_object_or_404(About, id=id) if id else None

    if request.method == "POST":
        form = AboutForm(request.POST, instance=about_instance)
        if form.is_valid():
            form.save()
            return redirect('about')  # Replace with your success URL or view name
    
    else:
        form = AboutForm(instance=about_instance)
    
    return render(request, 'edit_about.html', {'form': form})    




def edit_course(request, id=None):
    course_instance = get_object_or_404(Course, id=id) if id else None

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course_instance)
        if form.is_valid():
            form.save()
            return redirect('admin_course')  # Replace with your success URL or view name

    else:
        form = CourseForm(instance=course_instance)

    return render(request, 'edit_course.html', {'form': form})




def delete_course(request, id=None):
    if id:
        course = get_object_or_404(Course, id=id)
        course.delete()
        return redirect('admin_course')  # Redirect after deletion
    else:
        # Handle the case where no ID is provided (optional)
        return HttpResponse("No course ID provided", status=400)
    
    
def insert_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_course')  # Replace with your success URL or view name
    else:
        form = CourseForm()

    return render(request, 'insert_course.html', {'form': form})
    