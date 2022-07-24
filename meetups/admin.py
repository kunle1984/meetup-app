from django.contrib import admin
from .models import Meetup,Location,Participant, myUser, Speaker



# Register your models here.
class MeetupAdmin (admin.ModelAdmin):
   list_display=('title', 'slug',  )
   list_filter=('title',)
   prepopulated_fields={'slug':('title',)}
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)

admin.site.register(Participant)
admin.site.register(myUser)
admin.site.register(Speaker)