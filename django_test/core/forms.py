from django import forms

class MessageForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': '',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message...',
        'class': '',
    }))