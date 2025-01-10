from django.contrib import admin
from .models import Categoria, Autor, Prestamo, Libro

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
    list_filter = ('nacionalidad',)
admin.site.register(Autor, AutorAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    search_fields = ('nombre', )

admin.site.register(Categoria, CategoriaAdmin)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disponible', 'fecha_publicacion')
    search_fields = ('titulo', )
    list_filter = ('disponible', 'fecha_publicacion')
    date_hierarchy = 'fecha_publicacion'


admin.site.register(Libro, LibroAdmin)


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'prestado_a', 'devuelto', 'fecha_prestamo')
    search_fields = ('libro__titulo', 'prestado_a')
    list_filter = ('libro', 'devuelto', 'fecha_devolucion')
    date_hierarchy = 'fecha_prestamo'

admin.site.register(Prestamo, PrestamoAdmin)