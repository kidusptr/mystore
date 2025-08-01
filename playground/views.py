from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import mail_admins, BadHeaderError
import os


def index(request):
    try:
        html_path = os.path.join(os.path.dirname(__file__), "email.html")
        with open(html_path, "r") as f:
            html_content = f.read()

        mail_admins(
            subject="Test Email from Django",
            message="This is a fallback plain-text message.",
            html_message=html_content,
        )
        return HttpResponse("Test email sent to admins.")

    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    except FileNotFoundError:
        return HttpResponse("Email template file not found.")
