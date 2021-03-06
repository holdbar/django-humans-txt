# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/__init__.py


from humans_txt.models.person import Person
from humans_txt.models.standard import Standard
from humans_txt.models.component import Component
from humans_txt.models.software import Software
from humans_txt.models.thank import Thank


__all__ = [
    "Person",
    "Standard",
    "Component",
    "Software",
    "Thank",
]
