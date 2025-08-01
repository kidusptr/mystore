from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
import os


def index(request):
    try:
        message = EmailMessage(
            "Subject",
            "Message",
            "kidus@localhost.com",
            ["test@localhost.com"],
        )
        message.attach_file(os.path.join("playground", "email.html"))
        message.send()
        return HttpResponse("Test email sent to admins.")

    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    except FileNotFoundError:
        return HttpResponse("Email template file not found.")
