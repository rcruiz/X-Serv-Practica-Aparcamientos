from django.conf.urls import include, url
from django.contrib import admin
from aparcamientos import views
from django.contrib.auth.views import login, logout
from django.views.static import serve
from project import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.mostrar_todo, name='Mostrar aparcamientos almacenados'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout', logout, {'next_page': '/'}),
    url(r'^login', login),
    url(r'^aparcamientos/(\d+)', views.aparca_id, name='Informacion del aparcamiento'),
    url(r'^aparcamientos', views.aparcamientos, name='Mostrar aparcamientos'),
    #url(r'^css$', views.css),
    #url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_URL }),
    #url(r'^(static/(?P<path>.*)$', serve, {'document_root':'templates/businessxhtml'}),
    url(r'^style.css$', serve, {'document_root':'templates/businessxhtml' }),
    #url(r'^about', views.autoria_html, name='Funcionamiento en HTML'),

    url(r'^(\w+)/xml', views.user_xml, name='Mostrar XML del usuario'),
    url(r'^(.+)', views.usuario, name='Mostrar pagina personal'),

    ## url(r'^(\w+)$', views.contenido, name='Accede y modifica contenido'),
    #url(r'^(.*)', views.contenido, name='Accede y modifica contenido'),
]
