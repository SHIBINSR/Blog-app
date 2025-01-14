from django.contrib import admin
from . models import Blog,Comments,Reply
 

admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(Reply)

# Register your models here.
