from mailchimp3 import MailChimp
from django.conf import settings


def get_mailchimp_api():
    return MailChimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user='username')

def subscribe_user(email):
    mailchimp = get_mailchimp_api()
    list_id = 'd779d47e7c'
    mailchimp.lists.members.create(list_id=list_id, data={'email_address': email, 'status': 'subscribed'})
