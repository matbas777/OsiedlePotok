from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.response import Response

from NaszeOsiedle.models import Inhabitant, Vote
from NaszeOsiedle.serializers import InhabitantSerializer, VoteSerializer, SingleVoteSerializer


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


class CreateVoteAPIView(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class ShowTheVoteAPIView(ListAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class CreateSingleVoteAPIView(CreateAPIView):
    serializer_class = SingleVoteSerializer
    queryset = Vote.objects.all()