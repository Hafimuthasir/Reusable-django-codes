from django.core.mail import send_mail

# Send a basic email
send_mail(
    'Subject',
    'Body',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)