from django import forms
from .models import About, Ceo, Course, CustomUser,Message,StudentRecord





class CeoForm(forms.ModelForm):
    class Meta:
        model = Ceo
        fields = ('name', 'description', 'image')


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'image', 'phone', 'first_name', 'last_name')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']        
        



class StudentRecordForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = [
            'first_name', 'middle_name', 'last_name', 'gender', 'month', 'email', 'course', 'phone_number', 'address', 
            'current_program', 'academic_performance', 'area_of_specializations', 'leadership_positions_held', 
            'duration_of_leadership_roles', 'leadership_achievements_and_responsibilities', 'year_of_study', 'age', 
            'value', 'state', 'country', 'resume_cv_upload', 'file_uploads', 'image'
        ]    
        
        
        
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }  
        
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_price', 'course_description', 'duration', 'start_date']
        widgets = {
            'course_description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }                  