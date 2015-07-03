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

    set('LANGUAGE_CODE', getattr(settings, 'LANGUAGE_CODE', 'en-us'))

    set('LOGIN_LOGO', login_logo)
    set('LOGIN_MESSAGE', login_message)
    set('LOGIN_FORM_ACTION', login_form_action)
    set('LOGIN_FORM_METHOD', login_form_method)
    set('LOGIN_USERNAME_IS_EMAIL', login_username_is_email)
    set('LOGIN_USERNAME_PLACEHOLDER', login_username_placeholder)
    set('LOGIN_PASSWORD_PLACEHOLDER', login_password_placeholder)
    set('LOGIN_REMEMBER_ME_TEXT', login_remember_me_text)
    set('LOGIN_SIGNIN_BTN_TEXT', login_signin_btn_text)
    set('LOGIN_HAS_SOCIAL', login_has_social)
    set('LOGIN_SOCIALS', login_socials)
    set('LOGIN_FORGOT_PASSWORD_URL', login_forgot_password_url)
    set('LOGIN_FORGOT_PASSWORD_TEXT', login_forgot_password_text)
    set('LOGIN_REGISTER_URL', login_register_url)
    set('LOGIN_REGISTER_TEXT', login_register_text)

    return alte_context
