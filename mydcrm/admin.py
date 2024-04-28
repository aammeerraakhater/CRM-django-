from django.contrib import admin
from .models import Record

# class RecordAdmin(admin.ModelAdmin):
#     fields = ["first_name", "phone"]


admin.site.register(Record)


