"""crimson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
#extra
#from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
#extra
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('', include("shop.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#extra
# class DirectTemplateView(TemplateView):
#     extra_context = None
#     def get_context_data(self, **kwargs):
#         context = super(self.__class__, self).get_context_data(**kwargs)
#         if self.extra_context is not None:
#             for key, value in self.extra_context.items():
#                 if callable(value):
#                     context[key] = value()
#                 else:
#                     context[key] = value
#         return context

# urlpatterns = patterns('',
#     url(r'^$', DirectTemplateView.as_view(template_name="index.html")), )
#extra