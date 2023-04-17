from django import forms

class Myform(forms.Form):
    rollno=forms.CharField(max_length=139)
    password=forms.CharField(max_length=139)
    conformpassword=forms.CharField(max_length=139)