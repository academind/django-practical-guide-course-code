from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
