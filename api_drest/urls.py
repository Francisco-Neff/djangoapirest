from django.urls import path,include
from . import views

urlpatterns = [
    path('view/',views.User_View.as_view(),name='view'),
    path('drest/<str:id>',views.UserCRUD_View.as_view(),name='drest')
]
