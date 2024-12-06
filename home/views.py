
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,Student, Customer
from .forms import BlogForm, StudentForm, CustumerForms

from django.contrib.auth.decorators import login_required

# Create your views here.
def blog (request):
    people = [
        {"name": "Ram Thapa", "age":60, "address": "Kathmandu, Nepal"},
        {"name": "Sita Gurung", "age": 25, "address": "Pokhara, Nepal"},
        {"name": "Bikash Rai", "age": 88, "address": "Lalitpur, Nepal"},
        {"name": "Pooja Shrestha", "age": 15, "address": "Bhaktapur, Nepal"},
        {"name": "Anil Magar", "age": 10, "address": "Biratnagar, Nepal"},
        {"name": "Nisha Tamang", "age": 27, "address": "Dharan, Nepal"},
        {"name": "Raju Khadka", "age": 40, "address": "Hetauda, Nepal"},
        {"name": "Sarita Maharjan", "age": 32, "address": "Chitwan, Nepal"},
    ]
    admin = [{"name" : "Dipen Shrestha", "address" : "Kathmandu"},
             {"name" : "Rahul Shrestha", "address" : "Pokhara"},
             ]
    
    text = "Hello my name is ..."
    return render(request, "blog.html", context = {'people': people, 'admin' : admin, 'text' : text})


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_html/blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_html/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_html/blog_form.html', {'form': form})

def blog_update(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_html/blog_form.html', {'form': form})

def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog_html/blog_confirm_delete.html', {'blog': blog})

def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'student_html/student_list.html', context={'student_list' : student_list})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_html/student_create.html', {'form': form})


# Customer 
@login_required
def customer_list(request):
    customer_list = Customer.objects.all()
    return render(request, 'customer_html/customer_list.html', context={'customer_list' : customer_list})

def customer_create(request):
    if request.method == 'POST':
        form = CustumerForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustumerForms()
    return render(request, 'customer_html/customer_create.html', {'form': form})


def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customer_html/customer_detail.html', {'customer': customer})

def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustumerForms(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustumerForms(instance=customer)
    return render(request, 'customer_html/customer_form.html', {'form': form})