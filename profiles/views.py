from django.core.exceptions import RequestAborted
from django.shortcuts import render, redirect
from django.template import context
from django.urls import reverse
from django.views import View
from profiles.forms import ProfileForm
# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm
        context = {'form':form}
        return render(request, "profiles/create_profile.html", context)

    def post(self, request):
        submitted_form =  ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid() ==True:
            return redirect(reverse('profiles'))

        return render(request,'profiles/create_profile.html',{'form':submitted_form})
        
