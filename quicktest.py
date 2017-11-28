import argparse
import sys

import django
from django.conf import settings, global_settings
from django.test.runner import DiscoverRunner as Runner


class QuickDjangoTest(object):
    """
    A quick way to run the Django test suite without a fully-configured project.
    Example usage:
        >>> QuickDjangoTest(apps=['app1', 'app2'])
    Based on a script published by Lukasz Dziedzia at:
    http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
    """

    def __init__(self, *args, **kwargs):
        self.apps = args
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
            'INSTALLED_APPS': [
                'django.contrib.staticfiles',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                'jstree',
            ],
            'STATIC_URL': '/static/',
            'TEMPLATES': [{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.media',
                        'django.template.context_processors.static',
                        'django.template.context_processors.tz',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
                'APP_DIRS': True,
            }],
            'LOGGING_CONFIG': None,
            'LOGGING': None,
            'FORCE_SCRIPT_NAME': None,
            'DEBUG': True,
            'DEFAULT_INDEX_TABLESPACE': None,
            'DEFAULT_TABLESPACE': None
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
        usage="[args]",
        description="Run Django tests on the provided applications."
    )
    parser.add_argument('apps', nargs='+', type=str)
    args = parser.parse_args()
    QuickDjangoTest(apps=args.apps)
