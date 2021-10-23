from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import XmlFileLinkForm
from .validator import is_xml_valid
from .service import get_link_content, save_xml, send_mail, update_xml_if_changed
from solution.models import UserXmlFile
from django.dispatch.dispatcher import receiver
from django.contrib.auth.signals import user_logged_in

@login_required()
def index(request):
	form = XmlFileLinkForm()
	context = {"form": form}

	if request.method == 'POST':
		form = XmlFileLinkForm(request.POST)

		if form.is_valid():
			xmlFileLink = form.cleaned_data["xmlFileLink"]
			xmlContent = get_link_content(xmlFileLink)

			if is_xml_valid(xmlContent):
				save_xml(request.user, xmlFileLink, xmlContent)
				context = {"form": form, "message": "XML File is valid. Saved to database."}
			else:
				send_mail()
				context = {"form": form, "message": "The File is invalid! Please check your email."}

	return render(request, "solution/index.html", context)

@receiver(user_logged_in, dispatch_uid="unique")
def user_logged_in(request, user, **kwargs):
	print('User logged in.')
	update_xml_if_changed(request.user)
