# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.staticfiles.templatetags.staticfiles import static

from os.path import join as pjoin

from ..settings import *

register = template.Library()

@register.simple_tag
def alte_load_css(*names):
    lines = []
    for name in names:
        url = None

        if name == 'bootstrap':
            url = pjoin(bootstrap_url_base, 'css/bootstrap.min.css')
        elif name == 'fontawesome':
            url = pjoin(fontawesome_url_base, 'css/font-awesome.min.css')
        elif name == 'ionicons':
            url = pjoin(ionicons_url_base, 'css/ionicons.min.css')
        elif name == 'adminlte':
            url = pjoin(adminlte_url_base, 'css/AdminLTE.min.css')

        if url:
            lines.append('<link href="%s" rel="stylesheet" type="text/css" />' % url)
    return '\n'.join(lines)

@register.simple_tag
def alte_load_js(*names):
    lines = []
    for name in names:
        url = None

        if name == 'jquery':
            url = jquery_url
        elif name == 'bootstrap':
            url = pjoin(bootstrap_url_base, 'js/bootstrap.min.js')
        elif name == 'adminlte':
            url = pjoin(adminlte_url_base, 'js/app.min.js')

        if url:
            lines.append('<script src="%s" type="text/javascript"></script>' % url)
    return '\n'.join(lines)

@register.simple_tag
def alte_load_skin_css():
    skinurl = pjoin(adminlte_url_base, 'css/skins/skin-%s.min.css' % skin)
    return '<link href="%s" rel="stylesheet" type="text/css" />' % skinurl

@register.simple_tag
def alte_load_plugin_css(*names):
    lines = []
    for name in names:
        url = None

        if name.startswith('iCheck/'):
            url = pjoin(adminlte_url_base, 'plugins/%s.css' % name)

        if url:
            lines.append('<link href="%s" rel="stylesheet" type="text/css" />' % url)
    return '\n'.join(lines)

@register.simple_tag
def alte_load_plugin_js(*names):
    lines = []
    for name in names:
        if name == 'iCheck':
            url = pjoin(adminlte_url_base, 'plugins/iCheck/icheck.min.js')

        if url:
            lines.append('<script src="%s" type="text/javascript"></script>' % url)
    return '\n'.join(lines)

@register.simple_tag
def alte_get_img_url(name):
    return pjoin(adminlte_url_base, name)
