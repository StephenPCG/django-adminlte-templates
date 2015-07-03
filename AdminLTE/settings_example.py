#!/usr/bin/env python
# -*- coding: utf-8 -*-

ADMINLTE_SETTINGS = {
    'STATIC': {
        # settings related to static resources
        'BOOTSTRAP_URL_BASE': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/', # set to None to use local bootstrap dist
        'FONTAWESOME_URL_BASE': '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/', # set to None to use local fontawesome dist
        'IONICONS_URL_BASE': 'http://code.ionicframework.com/ionicons/2.0.1/', # set to None to use local ionicons dist
        'ADMINLTE_URL_BASE': None, # usually you don't need to change this, set to None to use local adminlte dist
        'JQUERY_URL': '//code.jquery.com/jquery-2.1.4.min.js', # set to None to use local jquery dist
    },
    'THEME': {
        'SKIN': 'blue', # default AdminLTE skin color
    },
    'URL': {
        'LOGIN': '#', # login page url
        'LOGIN_FORM': '.', # login page form action url
        'REGISTER': '#', # register page url
        'REGISTER_FORM': '.', # register page form action url
        'FORGOT_PASSWORD': '#', # forgot password page url
        'TERMS': '#', # terms page url, set to None to hide 'I agree to the terms' link
    },
    'LOGIN': {
        # settings related to template: AdminLTE/login.html
        'PAGE_TITLE': 'AdminLTE 2 | Login Page', # login page title
        'LOGO': '<b>Admin</b>LTE', # login page logo, can use html
        'MESSAGE': 'Sign in to start your session', # Login page message, can use html
        'FORM_METHOD': 'post', # login form submit method
        'USERNAME_IS_EMAIL': True, # if True, will use email field for username input, otherwise use text field
        'USERNAME_PLACEHOLDER': 'Email', # placeholder for username input field
        'PASSWORD_PLACEHOLDER': 'Password', # placeholder for password input field
        'REMEMBER_ME_TEXT': 'Remember Me', # set to None to hide the 'Remember Me' check box
        'BUTTON_TEXT': 'Sign In', # text on signin button
        'SOCIALS': [{'name': 'google-plus', 'link': '#', 'text': 'Sign in using GooglePlus'},],
        # add social links, by default, SOCIALS is an empty list
        'FORGOT_PASSWORD_LINK_TEXT': 'I forgot my password', # the display text
        'REGISTER_LINK_TEXT': 'Register a new membership', # the display text
    },
    'REGISTER': {
        'PAGE_TITLE': 'AdminLTE 2 | Registration Page', # registration page title
        'LOGO': '<b>Admin</b>LTE', # registration page logo, can use html
        'MESSAGE': 'Register a new membership', # registration page message, can use html
        'FORM_METHOD': 'post', # registration page form method
        'FIELDS': [{'name': 'fieldname', 'type': 'text', 'placeholder': 'placeholder', 'glyphicon': 'icon'},],
        # registion fields, by default there are 4 fields: fullname, email, password, password2
        'AGREE_TERMS_TEXT': 'I agree to the <a href="#">Terms</a>', # text of agree to terms link, can use html
        'BUTTON_TEXT': 'Register', # text on register button
        'LOGIN_LINK_TEXT': 'I already have a membership', # the display text
    },
}
