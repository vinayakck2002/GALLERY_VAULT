from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.signin,name='signin'),
    path('signup',views.usersignup,name='signup'),
    path('helo',views.index,name='hlw'),


    path('gv',views.viewsmain,name='namemain'),
    path('delete/<pk>',views.delete,name='urdelete'),
    path('addimage',views.add,name='add'),
    path('pic/<id>',views.picture,name='pic')
]

# This line ensures media files are served during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
