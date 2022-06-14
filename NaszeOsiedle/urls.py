from django.urls import path
from django.contrib.auth import views as auth_views

from NaszeOsiedle.views import CreateInhabitantAPIView, DeleteInhabitantAPIView, CreateVoteAPIView, \
    CreateSingleVoteAPIView, ShowTheVoteAPIView

urlpatterns = [
    path('new_citizen', CreateInhabitantAPIView.as_view(), ),
    path('delete_citizen/<int:pk>', DeleteInhabitantAPIView.as_view(), ),
    path('new_vote', CreateVoteAPIView.as_view(), ),
    path('singlevote', CreateSingleVoteAPIView.as_view(), ),
    path('vote', ShowTheVoteAPIView.as_view(), ),

    path('reset_password', auth_views.PasswordResetView.as_view(),),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(),),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),)
]