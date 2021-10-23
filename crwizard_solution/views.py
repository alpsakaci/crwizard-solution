from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import XmlFileLinkForm

@login_required()
def index(request):
	if request.method == 'POST':
		form = XmlFileLinkForm(request.POST)

		if form.is_valid():
			xmlFileLink = form.cleaned_data["xmlFileLink"]
			print(xmlFileLink)

	form = XmlFileLinkForm()
	context = {"form": form}

	return render(request, "index.html", context)
