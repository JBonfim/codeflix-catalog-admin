from rest_framework import serializers

from core.cast_member.domain.cast_member import CastMemberType


class CastMemberTypeField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        choices = [(type.name, type.value) for type in CastMemberType]
        super().__init__(choices=choices, **kwargs)

    def to_internal_value(self, data):
        return CastMemberType(super().to_internal_value(data))

    def to_representation(self, value):
        return str(super().to_representation(value))


class CastMemberResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=255)
    type = CastMemberTypeField(required=True)
    
class ListOutputMetaSerializer(serializers.Serializer):
    current_page = serializers.IntegerField()
    per_page = serializers.IntegerField()
    total = serializers.IntegerField()


class ListCastMemberResponseSerializer(serializers.Serializer):
    data = CastMemberResponseSerializer(many=True)
    meta = ListOutputMetaSerializer()


class CreateCastMemberRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = CastMemberTypeField(required=True)


class CreateCastMemberResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class UpdateCastMemberRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    type = CastMemberTypeField(required=True)


class DeleteCastMemberRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField()