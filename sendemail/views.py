from django.shortcuts import render, redirect
from .forms import ContactForm
from dmail.settings import RECIPIENT_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            massage = form.cleaned_data['massage']
            try:
                send_mail(f'{subject} от {from_email}', massage, DEFAULT_FROM_EMAIL, RECIPIENT_EMAIL)
            except:
                return HttpResponse('Ошибка при отправки')
            return redirect('success')
    else:
        return HttpResponse('Ошибка при отправки')
    return render(request, 'email.html', {'form':form})

def success_view(request):
    return HttpResponse('Ваша зявка принета. Скоро мы с вами свяжемся')