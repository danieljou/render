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