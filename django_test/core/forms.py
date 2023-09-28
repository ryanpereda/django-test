from django import forms

class MessageForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl border',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message...',
        'class': 'w-full py-4 px-6 rounded-xl border',
    }))