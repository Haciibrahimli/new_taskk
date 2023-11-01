from django import forms
from my_app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mail', 'tel', 'mesage')

    def __init__(self, *args, **kwargs):
        super(ContactForm , self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].required = True

            self.fields['name'].widget.attrs.update({'placeholder':'adiniz'})
            self.fields['mail'].widget.attrs.update({'placeholder':'E-mailiniz'})
            self.fields['tel'].widget.attrs.update({'placeholder':'telefon nomreniz'})
            self.fields['mesage'].widget.attrs.update({'placeholder':'mesajlariniz'})
        