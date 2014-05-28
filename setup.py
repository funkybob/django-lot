# -*- coding: utf-8 -*-
from setuptools import setup
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

description = """
Django Login over Token.
"""

setup(
    name = "django-lot",
    url = "https://github.com/funkybob/django-lot",
    author = "Jesús Espino, Curtis Maloney",
    author_email = "curtis@tinbrain.net",
    version=':versiontools:lot:',
    packages = [
        "lot",
    ],
    description = description.strip(),
    install_requires=['django >= 1.6',],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    zip_safe=False,
    include_package_data = False,
    package_data = {},
    test_suite = 'nose.collector',
    tests_require = ['nose >= 1.2.1', 'django >= 1.6'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
