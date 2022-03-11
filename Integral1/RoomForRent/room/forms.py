from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms

from .models import Room,RentedRooms,Queries

# from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['owner']

        widgets = {
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'contact_details':forms.NumberInput(attrs={'class':'form-control'}),
            'room_type':forms.Select(attrs={'class':'form-control'}),
            'images':forms.URLInput(attrs={'class':'form-control'})
        }

class RentedForm(ModelForm):
    class Meta:
        model = RentedRooms
        fields = '__all__'
        exclude = ['buyer_username','odered_date','room_id']        

class QueriesForm(ModelForm):
    class Meta:
        model = Queries
        fields = '__all__'
        exclude = ['username']

        widgets = {
            'room_id':forms.Select(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'problem':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2')

    def __init__(self,*args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

