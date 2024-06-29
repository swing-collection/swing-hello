# -*- coding: utf-8 -*-


# Docstring
"""
Provides hello_template_view Function and HelloTemplateView Class.

...

Todo:
-----

Links:
------

"""


# Import | Standard Library


# Import | Libraries
from django.shortcuts import render
# from django.views import View
from django.views.generic.base import TemplateView


# Import | Local Modules


def hello_template_view(request,):
    """
    Hello Template View Definition
    """
    context = {
        "title": "Hello!",
        "content": "Lorem ipsum dolor sit amet",
    }
    return render(
        request,
        "hello.html",
        context
    )


class HelloTemplateView(TemplateView):
    """
    Hello Template View Class
    """

    template_name = "hello.html"

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        """
        Returns context.
        """
        context             = super().get_context_data(**kwargs)
        context["title"]    = "Hello!"
        context["content"]  = "Lorem ipsum dolor sit amet"
        return context
