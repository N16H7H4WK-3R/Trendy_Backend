from django.shortcuts import HttpResponse


def error_404_view(request, exception):
    content = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
                color: white;
                background-color: black;
            }
            h1 {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>404 Error</h1>
    </body>
    </html>
    """
    return HttpResponse(content)


def default(request):
    content = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
                color: white;
                background-color: black;
            }
            h1 {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Trendy_Backend HomePage</h1>
    </body>
    </html>
    """
    return HttpResponse(content)
