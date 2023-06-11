from django import forms

class ReviewForm(forms.Form):
    user_name=forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "You name must not to be empty",
        "max_length": "Please, enter a shorter name!"
    })