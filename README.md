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
