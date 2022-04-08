from django.contrib import admin
from .models import Log, EventType, MasterTable



class LogAdmin(admin.ModelAdmin):

    list_display = ('id', 'user_email', 'user_ip', 'event_question', 'event_type_id', 'intent', 'user_datetime')



class EventTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'description')



class MasterTableAdmin(admin.ModelAdmin):

    list_display = ('id', 'question', 'answer')



admin.site.register(Log, LogAdmin)

admin.site.register(EventType, EventTypeAdmin)

admin.site.register(MasterTable, MasterTableAdmin)







