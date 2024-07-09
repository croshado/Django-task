from django.shortcuts import render, redirect, get_object_or_404
from .models import Submission, ContactSubmission
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'index.html', {'time': current_time})

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        errors = {}

        if not name:
            errors['name'] = 'Name is required'
        if not email:
            errors['email'] = 'Email is required'

        if errors:
            return render(request, 'index.html', {'errors': errors, 'name': name, 'email': email, 'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        
        submission = Submission(name=name, email=email)
        submission.save()
        return render(request, 'submit.html', {'name': name, 'email': email})

def submissions(request):
    all_submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': all_submissions})

def delete_submission(request, id):
    submission = get_object_or_404(Submission, id=id)
    if request.method == 'POST':
        submission.delete()
        return redirect('submissions')
    return render(request, 'submissions.html')

def about(request):
    return render(request, 'about.html')




def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save form data to the database
        contact_submission = ContactSubmission(name=name, email=email, message=message)
        contact_submission.save()
        
        return redirect('contact_success')  # Redirect to a success page
    
    return render(request, 'contact_us.html')

def contact_success(request):
    return render(request, 'contact_success.html')