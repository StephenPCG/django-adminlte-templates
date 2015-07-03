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
        'APP_DIRS': True,                  # <--
        'OPTIONS': {
            'context_processors': [
                ...
                'AdminLTE.tcp.processor',  # <---
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

All adminlte settings are wrapped into a dict object named ``ADMINLTE_SETTINGS``,
you can check ``settings_example.py`` for all options.
You can ommit any portion if the default value is suitable for you,
but please carefully keep the structure.

Since there are too many configurations,
it's recommended that you store adminlte settings in an individual file, and import it from settings.py.
For example:

```
# adminlte_settings.py
ADMINLTE_SETTINGS = {
    ...
}

# settings.py
...
from adminlte_settings import ADMINLTE_SETTINGS
```

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
