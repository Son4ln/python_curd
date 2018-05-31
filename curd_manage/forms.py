from django import forms
from django.core import validators
from .models import Position
from django.contrib import messages


class PositionForm(forms.Form):
    name_attrs = {
        'class': 'form-control',
        'placeholder': 'Position Name'
    }

    name = forms.CharField(
        error_messages={'required': 'Please enter position name!'}, widget=forms.TextInput(attrs=name_attrs))

    def validator(self, request):
        if self.errors:
            for field in self:
                for error in field.errors:
                    messages.error(request, error, extra_tags='position_form_error')


class EmployeeForm(forms.Form):

    SEX = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other')
    )

    name = forms.CharField(
        error_messages={'required': 'Please enter employee name!'}, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))

    email = forms.EmailField(
        validators=[validators.EmailValidator(message='Invalid email')],
        required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    avatar = forms.ImageField(
        error_messages={'invalid_image': 'Please choice an image'},
        required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    address = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))

    sex = forms.ChoiceField(
        error_messages={'invalid_choice': 'Please choice Male or Female', 'required': 'Empty sex'},
        required=True, choices=SEX, widget=forms.Select(attrs={'class': 'form-control'}))

    positions = forms.ModelChoiceField(
        error_messages={'invalid_choice': 'Not a position', 'required': 'Empty position'},
        queryset=Position.objects.all(), to_field_name="id", empty_label="Select position", required=True,
        widget=forms.Select(attrs={'class': 'form-control'}))

    def validator(self, request):
        if self.errors:
            for field in self:
                for error in field.errors:
                    messages.error(request, error, extra_tags='employee_form_error')