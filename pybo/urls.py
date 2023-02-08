'''
파일명:urls.py
설 명:
생성일:2023-01-27
생성자:ohsunghun
since 2023.01.09 Copyright (C) by KandJamg All right reserved
'''


from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns =[
    #base
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),

    #answer
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    #answer_modify
    path('answer/modify/<int:answer_id>', views.answer_modify, name='answer_modify'),
    #answer_delete
    path('answer/delete/<int:answer_id>', views.answer_delete, name='answer_delete'),

    #question_create
    path('question/create/', views.question_create, name='question_create'),
    #question_modify
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    #question_delete
    path('question/delete/<int:question_id>', views.question_delete, name='question_delete'),

    #boot
    path('boot/menu',views.boot_menu,name='boot_menu'),
    path('boot/list',views.boot_list,name='boot_list'),
    path('boot/reg',views.boot_reg,name='boot_reg'),
    path('crawling/cgv',views.crawling_cgv,name='crawling_cgv')
]