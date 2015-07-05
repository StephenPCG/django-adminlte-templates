# -*- coding: utf-8 -*-

"""
Template Context Processor of AdminLTE templates.
"""

from django.conf import settings
from .settings import *

def processor(request):
    alte_context = dict()
    
    def set(key, value):
        key = 'ALTE_%s' % key
        alte_context[key] = value

    if callable(sidebar_generator):
        set('SIDEBAR', sidebar_generator(request))

    set('LANGUAGE_CODE', getattr(settings, 'LANGUAGE_CODE', 'en-us'))

    set('URL_LOGIN', url_login)
    set('URL_LOGIN_FORM', url_login_form)
    set('URL_LOGOUT', url_logout)
    set('URL_PROFILE', url_profile)
    set('URL_REGISTER', url_register)
    set('URL_REGISTER_FORM', url_register_form)
    set('URL_FORGOT_PASSWORD', url_forgot_password)
    set('URL_TERMS', url_terms)
    set('URL_PAGE_LOGO_HREF', url_page_logo_href)

    set('THEME_SKIN', skin)

    set('LOGIN_PAGE_TITLE', login_page_title)
    set('LOGIN_LOGO', login_logo)
    set('LOGIN_MESSAGE', login_message)
    set('LOGIN_FORM_METHOD', login_form_method)
    set('LOGIN_USERNAME_IS_EMAIL', login_username_is_email)
    set('LOGIN_USERNAME_PLACEHOLDER', login_username_placeholder)
    set('LOGIN_PASSWORD_PLACEHOLDER', login_password_placeholder)
    set('LOGIN_REMEMBER_ME_TEXT', login_remember_me_text)
    set('LOGIN_BTN_TEXT', login_btn_text)
    set('LOGIN_HAS_SOCIAL', login_has_social)
    set('LOGIN_SOCIALS', login_socials)
    set('LOGIN_FORGOT_PASSWORD_LINK_TEXT', login_forgot_password_link_text)
    set('LOGIN_REGISTER_LINK_TEXT', login_register_link_text)

    set('REGISTER_PAGE_TITLE', register_page_title)
    set('REGISTER_LOGO', register_logo)
    set('REGISTER_MESSAGE', register_message)
    set('REGISTER_FORM_METHOD', register_form_method)
    set('REGISTER_FIELDS', register_fields)
    set('REGISTER_AGREE_TERMS_TEXT', register_agree_terms_text)
    set('REGISTER_BTN_TEXT', register_btn_text)
    set('REGISTER_LOGIN_LINK_TEXT', register_login_link_text)

    set('PAGE_LOGO_LG', page_logo_lg)
    set('PAGE_LOGO_MINI', page_logo_mini)

    return alte_context
