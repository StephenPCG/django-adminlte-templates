## This project is abandoned

I'm sorry for not responding to Issues of this project. this project was abandoned a long time ago.

I'm an OPS, and mostly work on backend tasks. A few years ago I need to write a simple dashboard,
so started this project, however, shorly, the dashboard was deprecated and so was this project.
I have not plan to re-pickup this projet.

Django's API had changed a lot during these years, this project is no longer compatible with the latest
django. As per a simple trying, this project can only work with ``django==1.8``, not with any prior
or later versions.

Is it valuable to fork and continue this project? Personally, I think NO. AdminLTE is purely a frontend
project, the core of AdminLTE is its ``AdminLTE.css`` and ``app.min.js``. The html widgets templates is
just demo and documentation. The widgets can not easily be modulized and generalized into django plugin for
reuse (at least I don't have any good idea).

My suggestings: if you would like to use AdminLTE templates, you just need to import ``AdminLTE.css``, ``app.min.css``
and other third-party assets AdminLTE depends on. Or you can find a django plugin to do that for you, that
should be enough.

## Django AdminLTE Template

AdminLTE Bootstrap Theme packaged for Django

### Quick Start

Add ``AdminLTE`` to your ``INSTALLED_APPS`` setting like this:

```
INSTALLED_APPS = (
    ...
    'AdminLTE',
)
```

Install AdminLTE template context processor to djnago template engine like this:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # <--
        'OPTIONS': {
            'context_processors': [
                ...
                'AdminLTE.context_processors.processor',  # <---
            ],
        },
    },
]
```

It is almost done. You can check if this is working by adding a TemplateView against AdminLTE/login.html:

```
# urls.py

from django.views.generic.base import TemplateView

urlpatterns = [
        url('^someurl/$', TemplateView.as_view(template_name='AdminLTE/login.html'))
]
```

Visit ``/someurl/`` and you should see the default AdminLTE login page.

### Configuration

All template related settings can be initialized with a dict, in settings.py:

```
from AdminLTE.settings import Settings
Settings.load(
    {
        # settings ...
    }
)
```

These settings are only loaded on startup, no runtime changes are allowed.

Check ``AdminLTE/default_settings.py`` for all possible settings.

### Extends AdminLTE page templates

There are some example pages like 'login.html', 'register.html', etc. shipped,
you can use them directly, or you can extend the shipped one and do more customizations
which can not be done by simply changing configurations.

```
# app/templates/my-login.html
{% extends 'AdminLTE/login.html' %}
{% block html_head_title %}My Login Page{% endblock %}
...
```

### Template Tags

TODO

## About AdminLTE

**AdminLTE** -- is a fully responsive admin template. Based on **Bootstrap 3** framework. Highly customizable and easy to use. Fits many screen resolutions from small mobile devices to large desktops. Check out the live preview now and see for yourself.

**Live Preview: http://almsaeedstudio.com/preview/**
