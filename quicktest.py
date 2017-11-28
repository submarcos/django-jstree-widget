from __future__ import unicode_literals

import argparse
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner as Runner


class QuickDjangoTest(object):
    """
    A quick way to run the Django test suite without a fully-configured project.
    Example usage:
        >>> QuickDjangoTest(apps=['app1', 'app2'])
    Based on a script published by Lukasz Dziedzia at:
    http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
    """
    INSTALLED_APPS = [
        'django.contrib.staticfiles',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
    ]

    def __init__(self, *args, **kwargs):
        self.apps = kwargs.get('apps', [])
        self.run_tests()

    def run_tests(self):
        """
        Fire up the Django test suite
        """
        conf = {
            'DATABASES': {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'database.db',
                }
            },
            'INSTALLED_APPS': self.INSTALLED_APPS + self.apps,
            'STATIC_URL': '/static/',
            'TEMPLATES': {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                    ]
                },
                'APP_DIRS': True,
            }
        }

        settings.configure(**conf)
        django.setup()

        failures = Runner().run_tests(self.apps, verbosity=1)

        if failures:  # pragma: no cover
            sys.exit(failures)


if __name__ == '__main__':
    """
    What do when the user hits this file from the shell.
    Example usage:
        $ python quicktest.py app1 app2
    """
    parser = argparse.ArgumentParser(
        description="Run Django tests on the provided applications."
    )
    parser.add_argument('apps', nargs='+', type=str)
    args = parser.parse_args()
    QuickDjangoTest(apps=args.apps)
