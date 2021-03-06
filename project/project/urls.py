"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

logger = logging.getLogger('console')
def hello(request):
    content = '''
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            hello world
        </body>
    </html>
    '''
    logger.debug('test log from hello')
    return HttpResponse(content)

urlpatterns = [
    path('', include('welcome.urls')),
    path('memberships/', include('memberships.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('hello/', hello, name='hello'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

