from django.contrib import admin

from anti_profanity.models import Profanity


@admin.register(Profanity)
class ProfanityAdmin(admin.ModelAdmin):
    save_on_top = True
    save_on_bottom = False
    list_display = ('id', 'word')
    search_fields = ['word']
