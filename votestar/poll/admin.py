from django.contrib import admin
from .models import Question,Choice

# Register your models here.

#admin.site.register(Question)
#admin.site.register(Choice)

admin.site.site_header = 'Votestar Admin'
admin.site.site_title = 'Votestar Admin Area'
admin.site.site_header = 'Welcome To The Votestar Admin'

class ChoiceInLine(admin,TabularInLine):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)