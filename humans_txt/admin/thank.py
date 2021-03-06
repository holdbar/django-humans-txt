# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/admin/thank.py


from django.contrib import admin


__all__ = [
    "ThankAdmin",
]


class ThankAdmin(admin.ModelAdmin):
    """
    Customize Thank model for admin area.
    """

    list_display = ["name", "url", ]
    search_fields = ["name", "url", ]
