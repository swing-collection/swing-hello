# -*- coding: utf-8 -*-


# Docstring
"""
URL Configuration

...

Todo:
-----

Links:
------

"""


# Import | Futures
# […]

# Import | Standard Library
# […]

# Import | Libraries
from django.urls import path
# […]

# Import | Local Modules
from views import HelloResponseView
from views import HelloTemplateView
#from ..views import hello_response_view
#from ..views import hello_template_view
# # […]


# URL Patterns
urlpatterns = [
    #path('',                hello_response_view,            kwargs = None,      name='hello'),
    #path('response',        hello_response_view,            kwargs = None,      name='hello_response'),
    #path('template',        hello_template_view,            kwargs = None,      name='hello_template'),
    path('',                HelloTemplateView.as_view(),    kwargs = None,      name='hello'),
    path('response',        HelloResponseView.as_view(),    kwargs = None,      name='hello_response'),
    path('template',        HelloTemplateView.as_view(),    kwargs = None,      name='hello_template'),
]