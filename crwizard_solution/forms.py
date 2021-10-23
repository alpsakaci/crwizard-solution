from django import forms

class XmlFileLinkForm(forms.Form):
    xmlFileLink = forms.CharField(label='XML File Link')
