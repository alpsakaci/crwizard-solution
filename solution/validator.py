from lxml import etree

def is_xml_valid(xmlDoc):
	try:
		etree.fromstring(xmlDoc)
		return True
	except Exception:
		return False
