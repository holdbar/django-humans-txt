# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/models/thank.py


from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    "Thank",
]


class Thank(models.Model):
    """
    Thank model.
    """

    name = models.CharField(verbose_name=_("thank to person or organization name"), max_length=256, db_index=True)
    url = models.URLField(verbose_name=_("thank to person or organization site URL"), max_length=256, blank=True, null=True, db_index=True)

    class Meta:

        app_label = "humans_txt"
        verbose_name = _("thank")
        verbose_name_plural = _("thanks")
        ordering = ["name", ]

    def __unicode__(self) -> str:

        return self.name

    def __str__(self) -> str:

        return self.__unicode__()

    def __repr__(self) -> str:

        return self.__unicode__()
