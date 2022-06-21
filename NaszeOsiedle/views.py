from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from NaszeOsiedle.models import Inhabitant, Vote, Comment, Post
from NaszeOsiedle.serializers import InhabitantSerializer, VoteSerializer, SingleVoteSerializer, \
    UpdateInhabitantSerializer, CommentPostSerializer, PostSerializer, EditPostSerializer
import jwt, datetime


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Uzytkownik nieuwierzytelniony')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            return (Inhabitant.objects.get(pk=payload['id']), token)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Uzytkownik nieuwierzytelniony')


class CreateInhabitantAPIView(CreateAPIView):
    serializer_class = InhabitantSerializer
    queryset = Inhabitant.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(serializer.validated_data.get('password'))
        instance.save()
        return Response()


class DeleteInhabitantAPIView(RetrieveDestroyAPIView):
    serializer_class = InhabitantSerializer
    queryset = Inhabitant.objects.all()


class UpdateInhabitantAPIView(UpdateAPIView):
    serializer_class = UpdateInhabitantSerializer
    queryset = Inhabitant.objects.all()


class CreateVoteAPIView(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class ShowTheVoteAPIView(ListAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class CreateSingleVoteAPIView(CreateAPIView):
    authentication_classes = (APIKeyAuthentication,)
    serializer_class = SingleVoteSerializer
    queryset = Vote.objects.all()


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        user_name = request.data['user_name']
        password = request.data['password']

        user = Inhabitant.objects.filter(user_name=user_name).first()

        if not user:
            raise AuthenticationFailed('Nie prawidlowe dane do logowania')

        if not user.check_password(password):
            raise AuthenticationFailed('Nie prawidlowe dane do logowania')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt': token}

        return response


class LogoutUserView(APIView):
    def get(self, request, *args, **kwargs):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Wylogowany'
        }
        return response


class NewPostAPIView(CreateAPIView):
    authentication_classes = (APIKeyAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class NewCommentAPIView(CreateAPIView):
    authentication_classes = (APIKeyAuthentication,)
    serializer_class = CommentPostSerializer
    queryset = Comment.objects.all()


class EditPostAPIView(UpdateAPIView):
    authentication_classes = (APIKeyAuthentication,)
    serializer_class = EditPostSerializer

