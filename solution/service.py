import requests
from solution.models import UserXmlFile
import hashlib
from solution.validator import is_xml_valid

def get_link_content(link):
	try:
		content = requests.get(link).content
		return bytes.decode(content)
	except Exception:
		return None

def send_mail():
	print('sending mail')

def save_xml(user, url, xmlContent):
	user_xml, created = UserXmlFile.objects.get_or_create(owner = user)
	user_xml.url = url
	user_xml.xmlContent = xmlContent
	user_xml.save()

def hash_str(value):
    md5 = hashlib.new('md5')
    md5.update(bytes(value, 'utf'))
    
    return md5.hexdigest()

def is_files_equal(xml1, xml2):
	if hash_str(xml1).__eq__(hash_str(xml2)):
		return True
	else:
		return False

# TODO: run after auth
def update_xml_if_changed(user):
	xml = UserXmlFile.objects.filter(owner=user).first()

	if xml is not None:
		xmlContent = get_link_content(xml.url)

		if is_xml_valid(xmlContent):
			if not is_files_equal(xml.xmlContent, xmlContent):
				print('Xml updated.')
				xml.xmlContent = xmlContent
				xml.save()
