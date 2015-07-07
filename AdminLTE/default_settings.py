# -*- coding: utf-8 -*-

from .widgets.sidebar import Sidebar

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

DEFAULT_SETTINGS = {
    'SIDEBAR_GENERATOR': lambda request: Sidebar(),
    'STATIC': {
        # settings related to static resources
        # to use maxcdn, change None to: //maxcdn.bootstrapcdn.com/bootstrap/3.3.5/, default use local dist
        'BOOTSTRAP_URL_BASE': None,
        # to use maxcdn, change None to: //maxcdn.bootstrapcdn.com/font-awesome/4.3.0/
        'FONTAWESOME_URL_BASE': None,
        # to use cdn, change None to: //code.ionicframework.com/ionicons/2.0.1/
        'IONICONS_URL_BASE': None,
        # no famous cdn for this
        'ADMINLTE_URL_BASE': None,
        # to use cdn, change None to: //code.jquery.com/jquery-2.1.4.min.js
        'JQUERY_URL': None,
    },
    'THEME': {
        # default AdminLTE skin color
        'SKIN': 'blue',
    },
    'URL': {
        'HOME': '/',
        'LOGIN': '#', # login page url
        'LOGIN_FORM': '.', # login page form action url
        'LOGOUT': '#', # logout url
        'REGISTER': '#', # register page url
        'REGISTER_FORM': '.', # register page form action url
        'FORGOT_PASSWORD': '#', # forgot password page url
        'TERMS': '#', # terms page url, set to None to hide 'I agree to the terms' link
    },
    'LOGIN': {
        # settings used for template: AdminLTE/login.html
        # if you don't use it or don't extends it, just ignore this part
        # login page title
        'PAGE_TITLE': 'AdminLTE 2 | Login Page',
        # login page logo, can use html
        'LOGO': '<b>Admin</b>LTE',
        # Login page message, can use html
        'MESSAGE': 'Sign in to start your session',
        # login form submit method
        'FORM_METHOD': 'post',
        # if True, will use email field for username input, otherwise use text field
        'USERNAME_IS_EMAIL': True,
        # placeholder for username input field
        'USERNAME_PLACEHOLDER': 'Email',
        # placeholder for password input field
        'PASSWORD_PLACEHOLDER': 'Password',
        # set to None to hide the 'Remember Me' check box
        'REMEMBER_ME_TEXT': 'Remember Me',
        # text on signin button
        'BUTTON_TEXT': 'Sign In',
        'SOCIALS': [{'name': 'google-plus', 'link': '#', 'text': 'Sign in using GooglePlus'},],
        # add social links, by default, SOCIALS is an empty list
        'FORGOT_PASSWORD_LINK_TEXT': 'I forgot my password',
        'REGISTER_LINK_TEXT': 'Register a new membership',
    },
    'REGISTER': {
        # settings used for template: AdminLTE/register.html
        # if you don't use it or don't extends it, just ignore this part
        # registration page title
        'PAGE_TITLE': 'AdminLTE 2 | Registration Page',
        # registration page logo, can use html
        'LOGO': '<b>Admin</b>LTE',
        # registration page message, can use html
        'MESSAGE': 'Register a new membership',
        # registration page form method
        'FORM_METHOD': 'post',
        # registion fields, by default there are 4 fields: fullname, email, password, password2
        'FIELDS': _DEFAULT_REGISTER_FIELDS,
        # text of agree to terms link, can use html
        'AGREE_TERMS_TEXT': 'I agree to the <a href="#">Terms</a>',
        # text on register button
        'BUTTON_TEXT': 'Register',
        # the display text
        'LOGIN_LINK_TEXT': 'I already have a membership',
    },
    'PAGE': {
        # settings used for template: AdminLTE/page.html
        # if you don't use it or don't extends it, just ignore this part
        'LOGO_LG': '<b>Admin</b>LTE',
        'LOGO_MINI': '<b>A</b>LTE',
    }
}
