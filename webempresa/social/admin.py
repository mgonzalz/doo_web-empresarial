from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request: HttpRequest, obj: Any) -> tuple:
        if request.user.groups.filter(name="Personal").exists():
            return ("key", "name")
        else:
            return ()

admin.site.register(Link, LinkAdmin)
