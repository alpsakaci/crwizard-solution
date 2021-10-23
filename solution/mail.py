from django.core.mail import send_mail
from django.http import HttpResponse
import crwizard_solution.settings as settings

def send_email(subject, body, mail_to):
	print('Sending mail')
	response = send_mail(subject, body, settings.EMAIL_HOST_USER, [mail_to])
	return response
