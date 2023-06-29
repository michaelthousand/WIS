from django import forms

class ContactForm(forms.Form):
    required_css_class = 'required'

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=20, required=False)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget= forms.Textarea, max_length=2000)