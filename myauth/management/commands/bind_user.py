from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=4)
        group, created = Group.objects.get_or_create(
            name='profile_manager',
        )
        permision_profile = Permission.objects.get(
            codename='view_profile'
        )
        permision_logentry = Permission.objects.get(
            codename='view_logentry'
        )
        group.permissions.add(permision_profile)
        user.groups.add(group)
        user.user_permissions.add(permision_logentry)

        group.save()
        user.save()