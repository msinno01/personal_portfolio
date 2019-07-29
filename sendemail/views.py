from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                with mail.get_connection() as connection:
                    mail.EmailMessage("Message from Contact Page: %s" % subject, "From: %s, %s\nMessage: %s" % (name, email, message), email, ['msinnott123@gmail.com'],connection=connection,headers={'Reply-To':email}).send()
            except mail.BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return render(request, "success.html", {})
