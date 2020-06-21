from django.contrib import admin

from .models import Post, Lesson,Curse,CurseBuy, Nofication,Comment,CommentReply,CurseLanding,CurseLandingAsk

class CurseBuyAdmin(admin.ModelAdmin):
    list_display = ('buyer','parent')

class NoficationAdmin(admin.ModelAdmin):
    list_display = ('nof_date','nof_user','nof_text')

class CurseLandingAskAdmin(admin.ModelAdmin):
    list_display = ('parent','ask','answer')


admin.site.register(Post)
admin.site.register(Curse)
admin.site.register(CurseBuy,CurseBuyAdmin)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(CurseLanding)
admin.site.register(CurseLandingAsk,CurseLandingAskAdmin)
admin.site.register(Nofication,NoficationAdmin)


