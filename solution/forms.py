from django import forms

class XmlFileLinkForm(forms.Form):
    xmlFileLink = forms.URLField(label='XML File Link')
