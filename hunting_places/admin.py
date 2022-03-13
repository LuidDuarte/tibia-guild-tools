from django.contrib import admin
from .models import HuntingGround, Exiva, HuntingExiva


class HuntingExivaInline(admin.TabularInline):
    model = HuntingExiva
    extra = 0
    # filter_horizontal = ('hunt', )
    exclude = ('id', 'modified', )


@admin.register(HuntingGround)
class HuntingGroundAdmin(admin.ModelAdmin):
    inlines = (HuntingExivaInline, )
    readonly_fields = ('id', 'modified', )

@admin.register(Exiva)
class ExivaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'modified',)