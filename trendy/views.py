from django.shortcuts import HttpResponse


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