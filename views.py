from django.shortcuts import render

# Create your views here.

from .forms import ResumeUpload
from .models import UploadPdf
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.models import User
import mimetypes


def login_page(request): # for login page for user
    # Login To Teachers Details Form.

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("upload_pdf")
        else:
            return render(request, 'not_user.html',  {"msg": "User not registered..!"})
    return render(request, 'login.html', {})

def upload_pdf(request): # upload files folder for multiple files
    if request.method == "POST":
        form = ResumeUpload(request.POST, request.FILES)
        files = request.FILES.getlist('resumes')
        if form.is_valid():
            for f in files:
                file_instance = UploadPdf(resumes=f)
                file_instance.save()
    else:
        form = ResumeUpload()
    return render(request, 'index.html', {'form': form})

import os
from django.conf import settings
from django.http import HttpResponse, Http404


def download(request,path): #download files
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read())
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
        # return response
        return render(request,filename)


# , content_type="application/resumes"