from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSeriaizer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        if self.context.get('request').user == data['following']:
            raise serializers.ValidationError(
                'Подписка на самого себя невозможна!')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
