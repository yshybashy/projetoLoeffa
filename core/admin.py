from django.contrib import admin
from .models import Loefa

# Register your models here.
@admin.register(Loefa)
class LoefaAdmin(admin.ModelAdmin):
  list_display = ['id', 'like', 'gif', 'deslike', 'total']