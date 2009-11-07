# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
import re
import sys

"""
custom Fields
"""



    
"""
Forms
"""

class RegisterForm(forms.Form):
    """
    simple register Form
    """
    uNameField = forms.CharField(max_length=30, min_length=3,required=True, label='Username',
                                  help_text=u'Currently only alphanumeric characters and underscore allowed.')
    uPassField1 = forms.CharField(min_length=3, required=True, label='Password', 
                                  widget=forms.PasswordInput(render_value=False))
    uPassField2 = forms.CharField(min_length=3, required=True, label='Password (repeat)', 
                                  widget=forms.PasswordInput(render_value=False))
    uMailField = forms.EmailField(required=False, label='E-Mail', 
                                  help_text=u'Not required, but might be useful if you need a new password.')
    
    def clean_uPassField1(self):
        cleaned_data = self.cleaned_data
        p1 = cleaned_data.get('uPassField1')
        p2 = cleaned_data.get('uPassField2')
        if not p1:
            raise forms.ValidationError("Please enter your password.")
        return cleaned_data['uPassField1']
        
    def clean_uPassField2(self):
        cleaned_data = self.cleaned_data
        p1 = cleaned_data.get('uPassField1')
        p2 = cleaned_data.get('uPassField2')
        if not p2:
            raise forms.ValidationError("Please repeat your password.")
        if p1 != p2:
            print p1
            print p2
            raise forms.ValidationError("Your passwords are not identical.")
        return cleaned_data['uPassField2']
    
    def clean_uNameField(self):
        if not re.search('^\w+$', self.cleaned_data['uNameField']):
            raise forms.ValidationError(u'Username contains illegal characters.')
        else:
            try:
                newuser = User.objects.get(username=self.cleaned_data['uNameField'])
                raise forms.ValidationError(u'This username is already taken. Please choose another.')
            except User.DoesNotExist: #@UndefinedVariable
                return self.cleaned_data['uNameField']
            


class LoginForm(forms.Form):
    """
    simple login form
    """
    uNameField = forms.CharField(required=True, label='Username')
    uPassField = forms.CharField(required=True, label='Password', 
                                 widget=forms.PasswordInput(render_value=False))
    
    def clean_uNameField(self):
        try:
            newuser = User.objects.get(username=self.cleaned_data['uNameField'])
            return self.cleaned_data['uNameField']
        except User.DoesNotExist: #@UndefinedVariable
            raise forms.ValidationError(u'user does not exist')
        
    def clean_uPassField(self):
        pass
        return self.cleaned_data['uPassField']
    
    
    
class TicketForm(forms.Form):
    """
    new ticket form
    """
    victim = forms.CharField(50, label='victim')
    ship = forms.CharField(60, label='lost ship')
    kbLink = forms.URLField(label='killboard link', verify_exists=True,#turn off in case of performance issues
                            validator_user_agent='django url validator')
    notes = forms.CharField(500, label='notes', required=False, widget=forms.widgets.Textarea())
    
