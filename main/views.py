from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import *
def index(request):
    return redirect('login')

@login_required
def home(request):
    mails = Contact.objects.exclude(email = ' ' )
    return render(request,'mail.html', {'mails':mails})

@login_required
def phone(request):
    mails = Contact.objects.exclude(tel = "")
    return render(request,'mail.html', {'mails':mails,'tel':True})

@login_required
def message(request):
    mails = Contact.objects.exclude(email = ' ' )
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        messageMail = render_to_string('message.html', {'title': title,'message':message})
        contacts = Contact.objects.all()
        contacts_list =[]
        for item in contacts:
            if item.email != None and item.email not in contacts_list:
                contacts_list.append(item.email)


        send_mail(
            subject="Mainling Pro",
            message=messageMail,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=contacts_list,
            html_message=messageMail,
            # content_subtype='html'
        )
    return render(request,'send.html', {'mails':mails})



from rest_framework.serializers import ModelSerializer

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

@api_view(['POST'])
def insertUser(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        else:
            return Response(serializer.errors, status=400)


from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings

def send():
    message = render_to_string('reset_password_email.html', {'reset_password_link': reset_password_link,})

    # send_mail(
    #     subject="Reset Password",
    #     message=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[user.email  ],
    #     html_message=message,
    #     # content_subtype='html'
    # )