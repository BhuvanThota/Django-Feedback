from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review
# Create your views here.

############################################################################################

# def reviews(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/thank_you")

#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html", {'form':form})

############################################################################################

# class ReviewView(View):

#     def get(self, request):
#         form = ReviewForm()
    
#         return render(request, "reviews/review.html", {'form':form})

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/thank_you")
    
#         return render(request, "reviews/review.html", {'form':form})
############################################################################################

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = "/thank_you"

#     def form_valid(self, form: Any):
#         form.save()
#         return super().form_valid(form)
    
############################################################################################

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank_you"


############################################################################################
############################################################################################
############################################################################################

# class ThankYouView(View):
#     def get(self, request):
#         reviews = Review.objects.all()
#         if len(reviews) > 3:
#             reviews = reviews[::-1]
#             reviews = reviews[:3]
#         return render(request, "reviews/thank_you.html",{"reviews": reviews})

############################################################################################

class ThankYouView(ListView):
    template_name = 'reviews/thank_you.html'
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        reviews = super().get_queryset()
        reviews = reviews[::-1]
        if len(reviews) > 3:
            reviews = reviews[:3]

        return reviews

############################################################################################
############################################################################################
############################################################################################
