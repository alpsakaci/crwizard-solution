import requests
from solution.models import UserXmlFile


def get_link_content(link):
	try:
		return requests.get(link).content
	except Exception:
		return None

def send_mail():
	print('sending mail')

def save_xml(user, url, xmlContent):
	user_xml, created = UserXmlFile.objects.get_or_create(owner = user)
	user_xml.url = url
	user_xml.xmlContent = bytes.decode(xmlContent)
	user_xml.save()
