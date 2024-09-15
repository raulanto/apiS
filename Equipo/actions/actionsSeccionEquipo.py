from django.http import HttpResponse
import csv

def exportSeccionEquipo_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="secciones.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Usuario', 'Equipo'])

    for obj in queryset:
        writer.writerow([obj.id, obj.nombre, obj.fkequipo.usuario.username if obj.fkequipo and obj.fkequipo.usuario else None, obj.fkequipo.nombre if obj.fkequipo else None])

    return response

exportSeccionEquipo_csv.short_description = "Exportar como CSV"

