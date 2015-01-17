from django.core.management.base import NoArgsCommand

from allauth.account.models import EmailConfirmation

class Command(NoArgsCommand):
    help = 'Deletes expired e-mail confirmations.'

    def handle_noargs(self, **options):
        EmailConfirmation.objects.delete_expired_confirmations()
