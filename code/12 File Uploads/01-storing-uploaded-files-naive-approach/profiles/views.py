from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")

