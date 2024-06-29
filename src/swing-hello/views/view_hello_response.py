# -*- coding: utf-8 -*-


# Docstring
"""
Provides hello_response_view Function and HelloResponseView Class.

...

Todo:
-----

Links:
------

"""


# Import | Standard Library


# Import | Libraries
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Import | Local Modules


def hello_response_view(request):
    """
    Hello Response View Definition
    """
    context = "Hello!"
    return HttpResponse(
        context,
        content_type = "text/plain"
    )


class HelloResponseView(View):
    """
    Hello Response View Class
    """

    def get(self, request, *args, **kwargs):
        """
        Returns context.
        """
        context = "Hello!"
        return HttpResponse(
            context,
            content_type = "text/plain"
        )
