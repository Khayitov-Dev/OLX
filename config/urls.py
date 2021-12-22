"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('olx.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('dj_rest_auth.urls')), # new
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






"""


Siz Web dasturlash kursini qaysidir o'quv markazida tamomladingizmi? Endilikda Ish Topishingiz uchun sizdan faqat tajriba talab qilishyapdimi.
Sizda muammo tajribasizlikmi? Unday bo'lsa bizning loyiha aynan siz uchun.


Biz Jamoamiz bilan ayana siz uchun "Practical Adventure" loyihamizga start berdik!

Bizning yangi start up loyihalarimizga qatnashing va o'z tajribangizni oshiring. 


"""