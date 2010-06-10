from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def webmaster_meta_tag():
    """
    Call this tag with:
        {% load google_webmaster_tags %}
        {% webmaster_meta_tag %}
    Place this code somewhere in the <head> section of your html.
    """
    webmaster_key = settings.GOOGLE_WEBMASTER_KEY
    tag_html = '<meta name="google-site-verification" content="' + webmaster_key + '" />'
    return tag_html
