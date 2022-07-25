from django.utils import timezone
from rest_framework import serializers

from NaszeOsiedle.models import Inhabitant, Vote, SingleVote, Post, Comment


class IsLoggedInMixin:
    def validate(self, obj):
        user = obj.get('inhabitant')
        user_in = self.context['request'].user
        if not user == user_in:
            raise serializers.ValidationError('Aby dodac post musisz byc zalogowany')
        return obj

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

    def validate(self,obj):
        user = obj.get('inhabitant')
        user_in = self.context['request'].user
        if not user == user_in:
            raise serializers.ValidationError('Mozesz edytowac tylko swoje dane')
        return obj


class VoteSerializer(serializers.ModelSerializer):
    choice_yes = serializers.SerializerMethodField()
    choice_no = serializers.SerializerMethodField()
    choice_pauses = serializers.SerializerMethodField()

    def get_choice_yes(self, obj):
        choice_yes = SingleVote.objects.filter(vote_choice=SingleVote.VoteChoice.yes, vote=obj).count()
        return choice_yes

    def get_choice_no(self, obj):
        choice_no = SingleVote.objects.filter(vote_choice=SingleVote.VoteChoice.no, vote=obj).count()
        return choice_no

    def get_choice_pauses(self, obj):
        choice_pauses = SingleVote.objects.filter(vote_choice=SingleVote.VoteChoice.pauses, vote=obj).count()
        return choice_pauses

    def validate(self, obj):
        super_user = self.context['request'].user.is_superuser
        if not super_user:
            raise serializers.ValidationError('Nie masz uprawnien do stworzenia glosowania')
        return obj

    class Meta:
        extra_kwargs = {"start_date": {"read_only": True}}
        model = Vote
        fields = (
            "id",
            "vote_title",
            "description",
            "start_date",
            "end_date",
            "choice_yes",
            "choice_no",
            "choice_pauses"
        )


class SingleVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SingleVote
        fields = (
            "id",
            "vote",
            "inhabitant",
            "vote_choice",
        )

    def validate(self, obj):
        vote = obj.get('vote')
        user_in = obj.get('inhabitant')
        user = self.context['request'].user       #.is_superuser
        if vote.end_date < timezone.now():
            raise serializers.ValidationError('Termin glosowanie sie skonczyl. Nie mozna juz brac udzialu')
        if not user == user_in:
            raise serializers.ValidationError('Mozesz glosowac tylko za siebie')
        if SingleVote.objects.filter(vote=vote, inhabitant=user_in).exists():
            raise serializers.ValidationError('Glos moze byc oddany tylko raz')
        return obj


class PostSerializer(serializers.ModelSerializer, IsLoggedInMixin):

    class Meta:
        model = Post
        fields = (
            "id",
            "post_title",
            "description",
            "post_date",
            "image",
            "inhabitant"
        )




class CommentPostSerializer(serializers.ModelSerializer, IsLoggedInMixin):

    class Meta:
        model = Comment
        fields = (
            "id",
            "comment",
            "post",
            "comment_date",
            "image",
            "inhabitant"
        )




    # {
    #     "user_name": "502/1",
    #     "password": "mieszkanie502/1"
    # }

class EditPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "post_title",
            "description",
            "image"
        )

    def validate(self, obj):

        user = obj.get('inhabitant')
        user_in = self.context['request'].user
        if not user == user_in:
            raise serializers.ValidationError('Aby dodac post musisz byc zalogowany')
        if not Post.objects.filter(inhabitant=user_in):
            raise serializers.ValidationError('mozesz edytowac tylko swoj komentarz')
        return obj