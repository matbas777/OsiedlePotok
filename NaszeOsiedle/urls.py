from django.urls import path
from django.contrib.auth import views as auth_views

from NaszeOsiedle.views import CreateInhabitantAPIView, DeleteInhabitantAPIView, CreateVoteAPIView, \
    CreateSingleVoteAPIView, ShowTheVoteAPIView, LoginView, LogoutUserView, NewPostAPIView, NewCommentAPIView, \
    EditPostAPIView

urlpatterns = [
    path('new_citizen', CreateInhabitantAPIView.as_view(), ),
    path('login', LoginView.as_view(), ),
    path('logout', LogoutUserView.as_view(), ),
    path('delete_citizen/<int:pk>', DeleteInhabitantAPIView.as_view(), ),
    path('new_vote', CreateVoteAPIView.as_view(), ),
    path('singlevote', CreateSingleVoteAPIView.as_view(), ),
    path('vote', ShowTheVoteAPIView.as_view(), ),
    path('post', NewPostAPIView.as_view(), ),
    path('comment', NewCommentAPIView.as_view(), ),
    path('edit_post', EditPostAPIView.as_view(), ),

    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]