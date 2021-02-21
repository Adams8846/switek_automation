"""switek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
	#path('news/', include('news.urls', namespace = 'news')),
	path('ueditor/', include('DjangoUeditor.urls')),
	path('user/', include('user.urls')),
	#path('login/', include('login.urls')),
	#path('auto/', include('auto.urls', namespace = 'auto')),
	#path('robot/', include('robot.urls', namespace = 'robot')),
	path('solutions/', include('solutions.urls', namespace = 'solutions')),
	path('machinery/', include('machinery.urls', namespace = 'machinery')),
	path('blog/', include('blog.urls', namespace = 'blog')),
	path('contact/', include('contact.urls', namespace = 'contact')),
	#path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
	path('index/', include('index_en.urls', namespace='index_en')), 
	path('index_cn/', include('index_cn.urls', namespace='index_cn')),
	path('practice/', include('practice.urls', namespace='practice')),
]
