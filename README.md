# Swing | Hello

Swing Hello is a simple Django application that provides basic views to demonstrate response handling and template rendering. This package includes both function-based and class-based views for returning plain text and rendering templates with context.

## Features

- Function-based view returning a plain text "Hello!" response.
- Class-based view returning a plain text "Hello!" response.
- Function-based view rendering a template with a context.
- Class-based view rendering a template with a context.

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

- `hello_response_view`: Returns a plain text "Hello!" response.
- `hello_template_view`: Renders a template with a context.

### Class-Based Views

- `HelloResponseView`: Returns a plain text "Hello!" response.
- `HelloTemplateView`: Renders a template with a context.

### URL Patterns

The package provides the following URL patterns:

- `/hello/` - Renders the template with context using `HelloTemplateView`.
- `/hello/response` - Returns a plain text "Hello!" response using `HelloResponseView`.
- `/hello/template` - Renders the template with context using `HelloTemplateView`.

## Example Template

The package includes a simple HTML template `hello.html`:

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

## Project Structure

```
swing_hello/
    __init__.py
    admin.py
    apps.py
    models.py
    views/
        __init__.py
        view_hello_response.py
        view_hello_template.py
    templates/
        hello.html
    urls.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

Swing Hello is developed by Scape Agency. For any inquiries or support, please contact us at [info@scapeagency.com].
