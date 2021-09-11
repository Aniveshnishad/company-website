from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.test import TestCase

# Create your tests here.

EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER="anivesh.nishad@cubexo.io"
EMAIL_HOST_PASSWORD="9589957396@"
EMAIL_USE_SSL=False

#
# ctx = {
#                     'name': 'hi',
#                     'email': 'email',
#                     'reply': 'request'
#
#                 }
# message = get_template('manager/email-tamplate.html').render(ctx)
# msg = EmailMessage(
#                     "subject",
#                     message,
#                    EMAIL_HOST_USER,
#                     ['anivesh.nishad07@gmail.com'],
#
#                 )
# msg.content_subtype = "html"
# msg.send()

send_mail(
    subject="subject",
    message= "message",
    from_email=  EMAIL_HOST_USER,
    recipient_list=  ['anivesh.nishad07@gmail.com']
)