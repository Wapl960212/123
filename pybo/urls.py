'''
파일명:urls.py
설 명:
생성일:2023-01-27
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''


from django.urls import path
from .views import question_views, answer_views, boot_views, base_views

app_name = 'pybo'

urlpatterns =[
    #base
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    #answer_create
    path('answer/create/<int:question_id>', answer_views.answer_create, name='answer_create'),
    #answer_modify
    path('answer/modify/<int:answer_id>', answer_views.answer_modify, name='answer_modify'),
    #answer_delete
    path('answer/delete/<int:answer_id>', answer_views.answer_delete, name='answer_delete'),

    #question_create
    path('question/create/', question_views.question_create, name='question_create'),
    #question_modify
    path('question/modify/<int:question_id>', question_views.question_modify, name='question_modify'),
    #question_delete
    path('question/delete/<int:question_id>', question_views.question_delete, name='question_delete'),
    #question_vote
    path('question/vote/<int:question_id>', question_views.question_vote, name='question_vote'),

    #boot
    path('boot/menu',boot_views.boot_menu,name='boot_menu'),
    path('boot/list',boot_views.boot_list,name='boot_list'),
    path('boot/reg',boot_views.boot_reg,name='boot_reg'),
    path('crawling/cgv',boot_views.crawling_cgv,name='crawling_cgv')
]