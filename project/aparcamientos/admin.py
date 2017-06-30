from django.contrib import admin

from .models import Aparcamiento, AparcaSeleccionado, Comentario, Css

admin.site.register(Aparcamiento)
admin.site.register(AparcaSeleccionado)
admin.site.register(Comentario)
admin.site.register(Css)
