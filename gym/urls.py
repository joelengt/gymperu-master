from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from apps.blog.views import IndexView, ServiciosView, ClasesView, BlogView,VisitanosView,ContactanosView,ServiciosInteriorView,ClasesInteriorView,ClasesInterior2View

urlpatterns = [
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.blog.urls')),
    url(r'^api/', include('apps.clases.urls')),
    url(r'^api/', include('apps.servicios.urls')),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^servicios/$', ServiciosView.as_view(), name='servicios'),
    url(r'^servicios/entrenar/$',ServiciosInteriorView.as_view(), name='servicios-interior'),
    url(r'^servicios/nutricion/$',ServiciosInteriorView.as_view(), name='servicios-interior'),
    url(r'^servicios/convenio/$',ServiciosInteriorView.as_view(), name='servicios-interior'),
    url(r'^clases/$', ClasesView.as_view(), name='clases'),
    url(r'^clases/deportes-de-contacto/$', ClasesInteriorView.as_view(), name='clases-interior'),
    url(r'^clases/bestcicling/$', ClasesInteriorView.as_view(), name='clases-interior'),
    url(r'^clases/aerobicos/$', ClasesInteriorView.as_view(), name='clases-interior'),
    url(r'^clases/talleres/$', ClasesInteriorView.as_view(), name='clases-interior'),    
    url(r'^clases/deportes-de-contacto/1$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/deportes-de-contacto/2$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/deportes-de-contacto/3$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/deportes-de-contacto/4$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/deportes-de-contacto/5$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/deportes-de-contacto/6$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/deportes-de-contacto/7$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/bestcicling/1$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/bestcicling/2$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/bestcicling/3$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/1$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/2$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/3$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/4$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/5$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/6$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/7$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/aerobicos/8$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/talleres/1$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/talleres/2$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/talleres/3$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^clases/talleres/4$', ClasesInterior2View.as_view(), name='clases-interior2'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^visitanos/$', VisitanosView.as_view(), name='visitanos'),
    url(r'^contactanos/$', ContactanosView.as_view(), name='contactanos'),

]
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}), )
