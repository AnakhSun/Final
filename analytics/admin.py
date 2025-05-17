from django.contrib import admin
from .models import User, Fragment, Result

admin.site.register(User)
admin.site.register(Fragment)
admin.site.register(Result)