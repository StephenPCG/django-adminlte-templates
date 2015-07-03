# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

ADMINLTE_SETTINGS = getattr(settings, "ADMINLTE_SETTINGS", {})

def _get(key, default):
    frags = key.split('.')
    settings = ADMINLTE_SETTINGS

    for frag in frags:
        try:
            if frag.isdigit():
                frag = int(frag)
            settings = settings[frag]
        except:
            return default

    return settings

# bootstrap url base
_bootstrap_url_base = _get('STATIC.BOOTSTRAP_URL_BASE', None)
bootstrap_url_base = _bootstrap_url_base if _bootstrap_url_base else static('bootstrap')

# FontAwesome url base
_fontawesome_url_base = _get('STATIC.FONTAWESOME_URL_BASE', None)
fontawesome_url_base = _fontawesome_url_base if _fontawesome_url_base else static('Font-Awesome')

# ionicons url base
_ionicons_url_base = _get('STATIC.IONICONS_URL_BASE', None)
ionicons_url_base = _ionicons_url_base if _ionicons_url_base else static('ionicons')

# AdminLTE url base
_adminlte_url_base = _get('STATIC.ADMINLTE_URL_BASE', None)
adminlte_url_base = _adminlte_url_base if _adminlte_url_base else static('AdminLTE')

# jquery url base
_jquery_url = _get('STATIC.JQUERY_URL', None)
jquery_url = _jquery_url if _jquery_url else static('AdminLTE/plugins/jQuery/jQuery-2.1.4.min.js')

skin = _get('THEME.SKIN', 'blue')

login_logo = _get('LOGIN.LOGO', '<b>Admin</b>LTE')
login_message = _get('LOGIN.MESSAGE', 'Sign in to start your session')
login_form_action = _get('LOGIN.FORM_ACTION', '.')
login_form_method = _get('LOGIN.FORM_METHOD', 'post')
login_username_is_email = _get('LOGIN.USERNAME_IS_EMAIL', True)
login_username_placeholder = _get('LOGIN.USERNAME_PLACEHOLDER', 'Email')
login_password_placeholder = _get('LOGIN.PASSWORD_PLACEHOLDER', 'Password')
login_remember_me_text = _get('LOGIN.REMEMBER_ME_TEXT', 'Remember Me')
login_signin_btn_text = _get('LOGIN.SIGNIN_BUTTON_TEXT', 'Sign In')
login_socials = _get('LOGIN.SOCIALS', [])
login_has_social = len(login_socials) > 0
login_forgot_password_url = _get('LOGIN.FORGOT_PASSWORD_URL', '#')
login_forgot_password_text = _get('LOGIN.FORGOT_PASSWORD_TEXT', 'I forgot my password')
login_register_url = _get('LOGIN.REGISTER_URL', '#')
login_register_text = _get('LOGIN.REGISTER_TEXT', 'Register a new membership')
