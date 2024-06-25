from rest_framework import serializers
from pixi_db.sqlalchemy_models import SQLAlchemyConnectNE, SQLAlchemyDisconnectNE, SQLAlchemySendRCV, SQLAlchemyComparePairs

class ConnectNESerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    handle = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    hostname = serializers.CharField(max_length=100)
    port = serializers.IntegerField()
    interface = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return SQLAlchemyConnectNE(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance
    

class DisconnectNESerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    handle = serializers.CharField(max_length=100, allow_blank=True, required=False)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    hostname = serializers.CharField(max_length=100)
    port = serializers.IntegerField()
    interface = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return SQLAlchemyDisconnectNE(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance


class SendRCVSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    handle = serializers.CharField(max_length=100)
    command = serializers.CharField(max_length=500, allow_null=True, required=False)

    def create(self, validated_data):
        return SQLAlchemySendRCV(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance


class ComparePair_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stash = serializers.CharField(max_length=100)
    compare_input = serializers.CharField(max_length=150, allow_null=True, required=False)
    compare_result = serializers.CharField(max_length=150, allow_null=True, required=False)

    def create(self, validated_data):
        return SQLAlchemyComparePairs(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance
