from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(subject, amount, user, template):
  message = render_to_string(template, {
    'user': user,
    'amount': amount
  })

  send_mail = EmailMultiAlternatives(
    subject,
    '',
    to = [user.email]
  )

  send_mail.attach_alternative(message, 'text/html')

  send_mail.send()