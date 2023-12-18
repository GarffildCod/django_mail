from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='EMail', required=True)
    subject = forms.CharField(label='Тема', required=True)
    massage = forms.CharField(label='Сообщение', required=True)
