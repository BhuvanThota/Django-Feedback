from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import PorfileForm
from .models import UserProfile


# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

################################################################################################
################################################################################################

# class CreateProfileView(View):
#     def get(self, request):
#         form = PorfileForm
#         return render(request, "profiles/create_profile.html", {"form" : form})

#     def post(self, request):
#         submitted_form = PorfileForm(request.POST, request.FILES)  

#         if submitted_form.is_valid():
#             profile = UserProfile(image = request.FILES["user_image"])
#             profile.save()
#             return redirect("/profiles")

#         return render(request, "profiles/create_profile.html", {"form": submitted_form})


################################################################################################
################################################################################################


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles/"



class ProfilesView(View):
    def get(self, request):
        profiles = UserProfile.objects.all()
        return render(request, "profiles/user_profiles.html", {"profiles": profiles})