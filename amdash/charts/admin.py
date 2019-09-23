from django.contrib import admin
from .models import People, First_Name, Grouping
# Register your models here.


class GroupInline(admin.StackedInline):
    model = Grouping
    fk_name = 'from_group'

class PeopleAdmin(admin.ModelAdmin):
    inlines = [GroupInline]

admin.site.register(People)
admin.site.register(Grouping)
admin.site.register(First_Name)