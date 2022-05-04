from django.core.management import call_command
from django.core.management.base import BaseCommand

"""
This custom command is for loading the dumped data from the blockcain fixtures
"""


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")

        call_command(
            "loaddata", "db_admin_fixture.json"
        )  # to generate an admin user
        call_command("loaddata", "db_block_fixture.json")
        call_command("loaddata", "db_transaction_fixture.json")
