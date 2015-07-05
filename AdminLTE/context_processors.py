# -*- coding: utf-8 -*-

"""
Template Context Processor of AdminLTE templates.
"""

from .settings import Settings

def processor(request):
    alte_context = {
            'ALTE': Settings(),
        }

    return alte_context
