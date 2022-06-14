from rest_framework import serializers

from NaszeOsiedle.models import Inhabitant, Vote, SingleVote


class InhabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inhabitant
        fields = (
            "id",
            "user_name",
            "password",
            "first_name",
            "last_name",
            "e_mail",
            "flat_area",
        )


class UpdateInhabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inhabitant
        fields = (
            "first_name",
            "last_name",
            "e_mail",
        )


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"start_date": {"read_only": True}}
        model = Vote
        fields = (
            "id",
            "vote_title",
            "description",
            "start_date",
            "end_date"
        )


class SingleVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleVote
        fields = (
            "id",
            "vote",
            "inhabitant",
            "vote_choice"
        )