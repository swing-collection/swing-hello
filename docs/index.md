# Swing Hello

Swing Hello is a Django application that provides various views to demonstrate response handling, template rendering, JSON responses, form handling, and a simple API endpoint using Django Rest Framework. This package includes both function-based and class-based views.

## Features

- Function-based view returning a plain text "Hello!" response.
- Class-based view returning a plain text "Hello!" response.
- Function-based view rendering a template with a context.
- Class-based view rendering a template with a context.
- Function-based view returning a JSON response.
- Class-based view returning a JSON response.
- Function-based view handling a form.
- Class-based view handling a form.
- Simple API endpoint using Django Rest Framework.

## Installation

1. Ensure you have Django installed. If not, you can install it using pip:

   ```bash
   pip install django
   ```

2. Clone the repository or download the package and include it in your Django project.

## Setup

1. Add `swing_hello` to your Django project's `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'swing_hello',
   ]
   ```

2. Include the `swing_hello` URLs in your project's `urls.py`:

   ```python
   from django.urls import path, include

   urlpatterns = [
       ...
       path('hello/', include('swing_hello.urls')),
   ]
   ```

## Usage

### Function-Based Views

#### hello_response_view

A function-based view that returns a plain text "Hello!" response.

#### hello_template_view

A function-based view that renders a template with a context.

#### hello_json_view

A function-based view that returns a JSON response with a greeting message.

#### hello_form_view

A function-based view that displays a form and processes form submission.

### Class-Based Views

#### HelloResponseView

A class-based view that returns a plain text "Hello!" response.

#### HelloTemplateView

A class-based view that renders a template with a context.

#### HelloJsonView

A class-based view that returns a JSON response with a greeting message.

#### HelloFormView

A class-based view that displays a form and processes form submission.

#### HelloApiView

A simple API view using Django Rest Framework that returns a JSON response with a greeting message.

### URL Patterns

The package provides the following URL patterns:

- `/hello/` - Renders the template with context using `HelloTemplateView`.
- `/hello/response` - Returns a plain text "Hello!" response using `HelloResponseView`.
- `/hello/template` - Renders the template with context using `HelloTemplateView`.
- `/hello/json` - Returns a JSON response using `HelloJsonView`.
- `/hello/json_func` - Returns a JSON response using `hello_json_view`.
- `/hello/form` - Displays a form and processes form submission using `HelloFormView`.
- `/hello/form_func` - Displays a form and processes form submission using `hello_form_view`.
- `/hello/api` - A simple API endpoint returning a JSON response using `HelloApiView`.

### Example Templates

**hello.html**

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .container {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            margin-bottom: 20px;
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <p>{{ content }}</p>
    </div>
</body>
</html>
```

**hello_form.html**

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Form</title>
</head>
<body>
    <h1>Hello Form</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
```

## Testing

Run the tests using pytest to verify the functionality of the Swing Hello views.

**test_views.py**

```python
import pytest
from django.test import RequestFactory, HttpRequest
from django.http import HttpResponse, JsonResponse
from rest_framework.test import APIRequestFactory
from swing_hello.views import (
    hello_response_view,
    HelloResponseView,
    hello_template_view,
    HelloTemplateView,
)
from swing_hello.views.view_hello_json import hello_json_view, HelloJsonView
from swing_hello.views.view_hello_form import hello_form_view, HelloFormView
from swing_hello.views.view_hello_api import HelloApiView

@pytest.mark.django_db
class TestHelloResponseView:
    def setup_method(self) -> None:
        self.factory: RequestFactory = RequestFactory()

    def test_hello_response_view(self) -> None:
        request: HttpRequest = self.factory.get('/hello/response')
        response: HttpResponse = hello_response_view(request)
        assert response.status_code == 200
        assert response.content.decode() == "Hello!"

    def test_HelloResponseView(self) -> None:
        request: HttpRequest = self.factory.get('/hello/response')
        response: HttpResponse = HelloResponseView.as_view()(request)
        assert response.status_code == 200
        assert response.content.decode() == "Hello!"

@pytest.mark.django_db
class TestHelloTemplateView:
    def setup_method(self) -> None:
        self.factory: RequestFactory = RequestFactory()

    def test_hello_template_view(self) -> None:
        request: HttpRequest = self.factory.get('/hello/template')
        response: HttpResponse = hello_template_view(request)
        assert response.status_code == 200
        assert "Hello!" in response.content.decode()
        assert "Lorem ipsum dolor sit amet" in response.content.decode()

    def test_HelloTemplateView(self) -> None:
        request: HttpRequest = self.factory.get('/hello/template')
        response: HttpResponse = HelloTemplateView.as_view()(request)
        assert response.status_code == 200
        assert "Hello!" in response.content.decode()
        assert "Lorem ipsum dolor sit amet" in response.content.decode()

@pytest.mark.django_db
class TestHelloJsonView:
    def setup_method(self) -> None:
        self.factory: RequestFactory = RequestFactory()

    def test_hello_json_view(self) -> None:
        request: HttpRequest = self.factory.get('/hello/json_func')
        response: JsonResponse = hello_json_view(request)
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}

    def test_HelloJsonView(self) -> None:
        request: HttpRequest = self.factory.get('/hello/json')
        response: JsonResponse = HelloJsonView.as_view()(request)
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}

@pytest.mark.django_db
class TestHelloFormView:
    def setup_method(self) -> None:
        self.factory: RequestFactory = RequestFactory()

    def test_hello_form_view_get(self) -> None:
        request: HttpRequest = self.factory.get('/hello/form_func')
        response: HttpResponse = hello_form_view(request)
        assert response.status_code == 200
        assert "form" in response.content.decode()

    def test_hello_form_view_post(self) -> None:
        request: HttpRequest = self.factory.post('/hello/form_func', {'name': 'Alice'})
        response: HttpResponse = hello_form_view(request)
        assert response.status_code == 200
        assert "Hello, Alice!" in response.content.decode()

    def test_HelloFormView_get(self) -> None:
        request: HttpRequest = self.factory.get('/hello/form')
        response: HttpResponse = HelloFormView.as_view()(request)
        assert response.status_code == 200
        assert "form" in response.content.decode()

    def test_HelloFormView_post(self) -> None:
        request: HttpRequest = self.factory.post('/hello/form', {'name': 'Alice'})
        response: HttpResponse = HelloFormView.as_view()(request)
        assert response.status_code == 200
        assert "Hello, Alice!" in response.content.decode()

@pytest.mark.django_db
class TestHelloApiView:
    def setup_method(self) -> None:
        self.factory: APIRequestFactory = APIRequestFactory()

    def test_HelloApiView(self) -> None:
        request = self.factory.get('/hello/api')
        response = HelloApiView.as_view()(request)
        assert response.status_code == 200
        assert response.data == {"message": "Hello, World!"}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

Swing Hello is developed by Scape Agency. For any inquiries or support, please contact us at [info@scapeagency.com].
This documentation covers the new views, their purposes, and how to use them within the `Swing Hello` Django application. Feel free to further customize it to fit the specific details and requirements of your project.
