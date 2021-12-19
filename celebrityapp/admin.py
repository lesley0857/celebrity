from django.contrib import admin

# Register your models here.
from celebrityapp.models import *

admin.site.register(Customer),
admin.site.register(Posts),
admin.site.register(Comments),
admin.site.register(Replies),
admin.site.register(Team),
admin.site.register(Images),

