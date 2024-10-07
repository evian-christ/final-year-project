from django.contrib import admin
from django.urls import path, include

from futforall import views

urlpatterns = [
    path('admin/', admin.site.urls),            # connect 'admin/' to the builtin admin site
    path('account/', include('account.urls')),  # include the urls in urls.py of account app
    path('match/', include('match.urls')),      # include the urls in urls.py of match app
    path('notifc/', include('notifc.urls')),
    path('', views.index, name='index'),        # connect '' (deafult domain) to the index function in view
]
