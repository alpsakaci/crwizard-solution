import requests
from solution.models import UserXmlFile
import hashlib
from solution.validator import is_xml_valid
from lxml import etree

def get_link_content(link):
	try:
		content = requests.get(link).content
		return bytes.decode(content)
	except Exception:
		return None

def save_xml(user, url, xmlContent):
	user_xml, created = UserXmlFile.objects.get_or_create(owner = user)
	user_xml.url = url
	user_xml.xmlContent = xmlContent
	user_xml.save()

def get_summary(xmlContent):
	element_tree = etree.fromstring(bytes(xmlContent, 'utf8'))
	changed = 0
	for element in element_tree:
		el = element
		while len(el) is not 0:
			el = el[0]
		if el.text.__contains__("Blue"):
			el.text.replace("Blue", "Red")
			changed = changed + 1

	summary = f"The XML has {len(element_tree)} node. {changed} element replaced from Blue to Red"

	return (etree.tostring(element_tree), summary)

def hash_str(value):
    md5 = hashlib.new('md5')
    md5.update(bytes(value, 'utf'))
    
    return md5.hexdigest()

def is_files_equal(xml1, xml2):
	if hash_str(xml1).__eq__(hash_str(xml2)):
		return True
	else:
		return False

def update_xml_if_changed(user):
	xml = UserXmlFile.objects.filter(owner=user).first()

	if xml is not None:
		print('Checking xml file.')
		xmlContent = get_link_content(xml.url)

		if is_xml_valid(xmlContent):
			if not is_files_equal(xml.xmlContent, xmlContent):
				print('Xml updated.')
				xml.xmlContent = xmlContent
				xml.save()
