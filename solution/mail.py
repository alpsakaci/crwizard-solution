from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(subject, body, mail_to):
	print('Sending mail')
	res = send_mail(subject, body, "erenalpsakaci@gmail.com", [mail_to])
	return HttpResponse('%s'%res)