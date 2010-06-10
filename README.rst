.. -*- restructuredtext -*-

django-google-webmaster is a simple app to add the webmaster metadata into your django app

Installation
============

Download ``django-google-webmaster`` and put it on your python path.

Configuration
=============

Add this to your list of ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        ... 
        'google_webmaster',
        ...
    )

Go to the google webmaster site, create an account, and download the meta data key that is required for verification at https://www.google.com/webmasters/verification/home?hl=en

Use this key to set the variable in ``settings.py``::

    GOOGLE_WEBMASTER_KEY = 'your-key-G3eTxJZbETj4u_4Z0DoRfNWZc'

Usage
=====

In the <head> section of your html, include the following two lines::

    {% load google_webmaster_tags %}
    {% webmaster_meta_tag %}
