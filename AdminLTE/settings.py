# -*- coding: utf-8 -*-

from django.conf import settings as djangosettings

from .widgets.sidebar import Sidebar
from .default_settings import DEFAULT_SETTINGS

def store_get(store, key, default=None):
    frags = key.split('.')
    for frag in frags:
        try:
            if frag.isdigit():
                frag = int(frag)
            store = store[frag]
        except:
            return default
    return store

def store_set(store, key, value, only_if_nonexist=False):
    frags = key.split('.')

    for frag in frags[:-1]:
        if store.has_key(frag):
            store = store[frag]
        else:
            store[frag] = dict()
            store = store[frag]

    if only_if_nonexist and store.has_key(frags[-1]):
        return
    store[frags[-1]] = value

class SettingsBase(object):
    store = dict()
    instance_store = None
    loaded = False

    def iget(self, key, default=None):
        if not self.instance_store:
            self.instance_store = dict()

        class FakeDefault(): pass

        ret1 = store_get(self.instance_store, key, default=FakeDefault())
        ret2 = store_get(self.store, key, default=FakeDefault())

        if isinstance(ret1, FakeDefault):
            if isinstance(ret2, FakeDefault):
                return default
            else:
                return ret2

        if isinstance(ret1, dict) and isinstance(ret2, dict):
            ret1.update(ret2)

        return ret1

    def iset(self, key, value, only_if_nonexist=False):
        if not self.instance_store:
            self.instance_store = dict()
        return store_set(self.instance_store, key, value, only_if_nonexist)

    @classmethod
    def get(cls, key, default=None):
        return store_get(cls.store, key, default)

    @classmethod
    def set(cls, key, value, only_if_nonexist=False):
        store_set(cls.store, key, value, only_if_nonexist)

    @classmethod
    def _load(cls, settings, prefix=None):
        for key, value in settings.items():
            if not prefix:
                next_prefix = key
            else:
                next_prefix = prefix + '.' + key
            if isinstance(value, dict):
                cls._load(value, next_prefix)
            else:
                cls.set(next_prefix, value)

    @classmethod
    def load(cls, settings, prefix=None):
        if not cls.loaded:
            cls._load(settings, prefix)
            cls.loaded = True

        # adding extra settings
        cls.set('LOGIN.HAS_SOCIAL', len(cls.get('LOGIN.SOCIALS', []))>0)
        cls.set('LANGUAGE_CODE', getattr(djangosettings, 'LANGUAGE_CODE', 'en-us'), True)

class Meta(type):
    def __getitem__(self, key):
        return self.get(key)

class Settings(SettingsBase):
    store = DEFAULT_SETTINGS
    __metaclass__ = Meta

    def __getitem__(self, key):
        return self.iget(key)
