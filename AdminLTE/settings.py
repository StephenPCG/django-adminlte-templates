# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

from os.path import join as pjoin

ADMINLTE_SETTINGS = getattr(settings, "ADMINLTE_SETTINGS", {})

_DEFAULT_REGISTER_FIELDS = [
    {
        'name': 'fullname',
        'type': 'text',
        'placeholder': 'Full Name',
        'glyphicon': 'user',
    },
    {
        'name': 'username',
        'type': 'text',
        'placeholder': 'Email',
        'glyphicon': 'envelope',
    },
    {
        'name': 'password',
        'type': 'password',
        'placeholder': 'Password',
        'glyphicon': 'lock',
    },
    {
        'name': 'password2',
        'type': 'password',
        'placeholder': 'Retype Password',
        'glyphicon': 'log-in',
    },
]

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

navigation_menu_list = _get('NAVTREE', list())

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

url_login = _get('URL.LOGIN', '#')
url_login_form = _get('URL.LOGIN_FORM', '.')
url_logout = _get('URL.LOGOUT', '#')
url_profile = _get('URL.PROFILE', '#')
url_register = _get('URL.REGISTER', '#')
url_register_form = _get('URL.REGISTER_FORM', '.')
url_forgot_password = _get('URL.FORGOT_PASSWORD', '#')
url_terms = _get('URL.TERMS', '#')
url_page_logo_href = _get('URL.PAGE_LOGO_HREF', '/')

login_page_title = _get('LOGIN.PAGE_TITLE', 'AdminLTE 2 | Login Page')
login_logo = _get('LOGIN.LOGO', '<b>Admin</b>LTE')
login_message = _get('LOGIN.MESSAGE', 'Sign in to start your session')
login_form_method = _get('LOGIN.FORM_METHOD', 'post')
login_username_is_email = _get('LOGIN.USERNAME_IS_EMAIL', True)
login_username_placeholder = _get('LOGIN.USERNAME_PLACEHOLDER', 'Email')
login_password_placeholder = _get('LOGIN.PASSWORD_PLACEHOLDER', 'Password')
login_remember_me_text = _get('LOGIN.REMEMBER_ME_TEXT', 'Remember Me')
login_btn_text = _get('LOGIN.BUTTON_TEXT', 'Sign In')
login_socials = _get('LOGIN.SOCIALS', [])
login_has_social = len(login_socials) > 0
login_forgot_password_link_text = _get('LOGIN.FORGOT_PASSWORD_LINK_TEXT', 'I forgot my password')
login_register_link_text = _get('LOGIN.REGISTER_LINK_TEXT', 'Register a new membership')

register_page_title = _get('REGISTER.PAGE_TITLE', 'AdminLTE 2 | Registration Page')
register_logo = _get('REGISTER.LOGO', '<b>Admin</b>LTE')
register_message = _get('REGISTER.MESSAGE', 'Register a new membership')
register_form_method = _get('REGISTER.FORM_METHOD', 'post')
register_fields = _get('REGISTER.FIELDS', _DEFAULT_REGISTER_FIELDS)
if url_terms:
    register_agree_terms_text = _get('REGISTER.AGREE_TERMS_TEXT', 'I agree to the <a href="' + url_terms + '">Terms</a>')
else:
    register_agree_terms_text = None
register_btn_text = _get('REGISTER.BUTTON_TEXT', 'Register')
register_login_link_text = _get('REGISTER.LOGIN_LINK_TEXT', 'I already have a membership')

page_logo_lg = _get('PAGE.LOGO_LG', '<b>Admin</b>LTE')
page_logo_mini = _get('PAGE.LOGO_MINI', '<b>A</b>LTE')
