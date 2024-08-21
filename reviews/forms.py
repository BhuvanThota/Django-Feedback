from django import forms
from .models import *

# class ReviewForm(forms.Form):
#     username = forms.CharField( label = "Name", max_length=100, error_messages={
#         "required" : "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!(Max Length < 100)"
#     })

#     review_text = forms.CharField(label = "Feedback", widget = forms.Textarea, max_length=1000)

#     rating = forms.IntegerField(label = "Rating", min_value = 1, max_value = 5)

 
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields =  ['username', 'review_text', 'rating']
        fields  = '__all__' 
        # exclude = ['owner_text']
        labels = {"username": 'Name',
                  'review_text': 'Feedback',
                }
        error_messages = {
            "username":{
                "required" : "Your name must not be empty!",
                "max_length": "Please enter a shorter name!(Max Length < 100)"   
                }
            }
    rating = forms.IntegerField(label = "Rating", min_value = 1, max_value = 5)




