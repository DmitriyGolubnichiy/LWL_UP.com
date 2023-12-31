"""
URL configuration for Backend project.p

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('',  views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from services.views import (index,
                            me,
                            test_and_exercises,
                            log_in,contacts,
                            training_programs,
                            create)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index' ),
    path('services/', training_programs,name='training_programs'),
    path('me/', me,name='me'),
    path('test_and_exercises/', test_and_exercises,name='test_and_exercises'),
    path('log_in/', log_in,name='log_in'),
    path('contacts/', contacts,name='contacts'),
    path('create/',create,name='create')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
