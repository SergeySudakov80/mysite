import csv
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet


class ExportAsCSVmixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]
        responce = HttpResponse(content_type='text/csv')
        responce['Content-Disposition'] = 'attachment; filename={meta}-export.csv'
        csv_writer = csv.writer(responce)
        csv_writer.writerow(field_names)
        for obj in queryset:
            csv_writer.writerow([getattr(obj, field) for field in field_names])
        return responce
    export_csv.short_description = 'Export as CSV'
