from django import forms
from .models import Blog, Student, Customer

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'phone_no']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'phone_no']

class CustumerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'address', 'email','phone_no']
