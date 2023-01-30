from django import forms 
from .models import User_Rest

class User_Rest_Form(forms.ModelForm):
    id = forms.IntegerField(label='ID',required=True)
    class Meta:
        model = User_Rest
        fields = ['id','name_drest','email_drest']
    
    field_order = ['id','email_drest','name_drest']
