from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactMessage, Project


# HOME
def home(request):
    return render(request, 'main/home.html')


# SERVICES
def services(request):
    return render(request, 'main/services.html')


# WORK (PROJECTS)
def work(request):
    projects = Project.objects.all()
    return render(request, 'main/work.html', {'projects': projects})


# ABOUT
def about(request):
    return render(request, 'main/about.html')


# CONTACT
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save message
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email (console or real)
        send_mail(
            subject="We received your message - Space Technologies",
            message=f"Hi {name}, we received your message and will respond shortly.",
            from_email=None,
            recipient_list=[email],
            fail_silently=True,
        )

        # Success message
        messages.success(request, "✅ Your message has been sent successfully!")

        return redirect('contact')

    return render(request, 'main/contact.html')