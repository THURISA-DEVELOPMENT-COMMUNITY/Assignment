from django.urls import path
from collaboration.views import *


urlpatterns = [
    path('test_1/', test1),
    path('test_2/', test2),
    path('api_class/', APIViewTest.as_view()),
    path('collaborators/', CollaboratorView.as_view()),
]
