# -*- coding: utf-8 -*-

from optparse import make_option

from django.db import transaction
from django.core.management.base import NoArgsCommand

from temporary.models import Temporary


class Command(NoArgsCommand):

    option_list = NoArgsCommand.option_list + (
        make_option(
            '-n', '--dry-run',
            action='store_true', dest='dry_run', default=False,
            help="Do everything except database commit.",
        ),
    )

    help = "Can be run as a cronjob or directly to clean out expired temporary objects."

    def handle_noargs(self, **options):
        self.verbose = options.get('verbosity', 0)
        self.dry_run = options.get('dry_run', False)

        with transaction.atomic():
            for t in Temporary.orphans.order_by('pub_date'):
                if t.is_expired is False:
                    if self.verbose >= 1:
                        self.stdout.write(
                            "Skipping temporary object #%d\n" % t.pk)
                    continue

                if self.verbose >= 1 and not self.dry_run:
                    self.stdout.write(
                        "Deleting temporary object #%d\n" % t.pk)
                if self.dry_run and self.verbose >= 1:
                    self.stdout.write("Pretending to delete temporary object #%d \n" % t.pk)
                if not self.dry_run:
                    t.delete()
