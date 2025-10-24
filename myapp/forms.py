from django import forms
from myapp.models import Contact
from myapp.models import NewsLetter
from captcha.fields import CaptchaField

'''class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)'''

class ContactForm(forms.ModelForm):
    # subject field is not needed to be fiiled
    subject = forms.CharField(max_length=255,required=False)
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = NewsLetter
        fields = '__all__'