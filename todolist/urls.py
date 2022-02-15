from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.work_space, name='work_space'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('mark_complete/<int:todo_id>', views.mark_complete, name="mark_complete"),
    path('mark_incomplete/<int:todo_id>', views.mark_incomplete, name="mark_incomplete"),
    path('edit/<int:todo_id>', views.edit, name="edit"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
