from django.urls import path
from . import views
app_name = 'pybo'

urlpatterns =[
    path('',views.main, name = 'main'),
    path('<title>',views.quiz1, name = 'q'),
    #path('<det>',views.render_quiz, name='quiz'),
    path('<det>/<d>',views.render_quiz, name='quiz')
]