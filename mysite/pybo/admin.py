from django.contrib import admin
from .models import *


class QuizAdmin(admin.ModelAdmin):
    search_fields = ['title']

class DAdmin(admin.ModelAdmin):
    search_fileds = ['tit', 'ques', 'content1', 'content2', 'content3', 'content4', 'content5']

class SaveDataAdmin(admin.ModelAdmin):
    search_fileds = ['tit','email','content1', 'content2', 'content3', 'content4', 'content5','content6', 'content7', 'content8', 'content9', 'content10']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(D, DAdmin)
admin.site.register(SaveData, SaveDataAdmin)
