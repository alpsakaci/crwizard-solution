from lxml import etree

def is_xml_valid(xmlDoc):
	try:
		etree.fromstring(bytes(xmlDoc, 'utf8'))
		print('Xml is valid')
		return True
	except Exception as e:
		print('Xml is not valid')
		print(e)
		return False
