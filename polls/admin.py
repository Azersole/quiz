from django.contrib import admin

from .models import Question, Choice, Survey

admin.site.site_header = "Administration"
admin.site.site_title = "Administration Area"
admin.site.index_title = "Welcome to the administration area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Survey', {'fields': ['survey']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey)