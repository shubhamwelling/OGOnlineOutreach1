from django.contrib import admin

from .models import Post, FAQ, Events, Feedback

admin.site.register(Post)
admin.site.register(FAQ)
admin.site.register(Events)
admin.site.register(Feedback)