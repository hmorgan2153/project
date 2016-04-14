"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'Site16.views.home', name='home'),
    url(r'^contact/$', 'Site16.views.contact', name='contact'),
    url(r'^dcmain/$', 'src.views.dcmain', name='dcmain'),
    url(r'^big_data/$', 'src.views.big_data', name='big_data'),
    url(r'^data_architecture/$', 'src.views.data_architecture', name='data_architecture'),
    url(r'^BI_MI/$', 'src.views.BI_MI', name='BI_MI'),
    url(r'^Master_Data/$', 'src.views.Master_Data', name='Master_Data'),
    url(r'^Data_Q/$', 'src.views.Data_Q', name='Data_Q'),
    url(r'^PSmain/$', 'src.views.PSmain', name='PSmain'),
    url(r'^books/$', 'src.views.books', name='books'),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
