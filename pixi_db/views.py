from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from sqlalchemy.orm import sessionmaker
from pixi_db import sqlalchemy_models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pixi_db.sqlalchemy_models import SQLAlchemyConnectNE, SQLAlchemyDisconnectNE, SQLAlchemySendRCV, SQLAlchemyComparePairs
from pixi_db.serializers import ConnectNESerializer, DisconnectNESerializer, SendRCVSerializer, ComparePair_Serializer

Session = sessionmaker(bind=sqlalchemy_models.engine)

@method_decorator(csrf_exempt, name='dispatch')
class SQLAlchemyConnectNEAPIView(APIView):
    def get(self, request):
        session = Session()
        queryset = session.query(SQLAlchemyConnectNE).all()
        serializer = ConnectNESerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConnectNESerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            instance = SQLAlchemyConnectNE(**serializer.validated_data)
            session.add(instance)
            session.commit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        session = Session()
        instance = session.query(SQLAlchemyConnectNE).get(pk)
        return instance

    def get(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = ConnectNESerializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = ConnectNESerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = ConnectNESerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            session = Session()
            session.delete(instance)
            session.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class SQLAlchemyDisconnectNEAPIView(APIView):
    def get(self, request):
        session = Session()
        queryset = session.query(SQLAlchemyDisconnectNE).all()
        serializer = DisconnectNESerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisconnectNESerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            instance = SQLAlchemyDisconnectNE(**serializer.validated_data)
            session.add(instance)
            session.commit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        session = Session()
        instance = session.query(SQLAlchemyDisconnectNE).get(pk)
        return instance

    def get(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = DisconnectNESerializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = DisconnectNESerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = DisconnectNESerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            session = Session()
            session.delete(instance)
            session.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@method_decorator(csrf_exempt, name='dispatch')
class SQLAlchemySendRCVAPIView(APIView):
    def get(self, request):
        session = Session()
        queryset = session.query(SQLAlchemySendRCV).all()
        serializer = SendRCVSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SendRCVSerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            instance = SQLAlchemySendRCV(**serializer.validated_data)
            session.add(instance)
            session.commit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        session = Session()
        instance = session.query(SQLAlchemySendRCV).get(pk)
        return instance

    def get(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = SendRCVSerializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = SendRCVSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = SendRCVSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            session = Session()
            session.delete(instance)
            session.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@method_decorator(csrf_exempt, name='dispatch')
class SQLAlchemyComparePairsAPIView(APIView):
    def get(self, request):
        session = Session()
        queryset = session.query(SQLAlchemyComparePairs).all()
        serializer = ComparePair_Serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComparePair_Serializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            instance = SQLAlchemyComparePairs(**serializer.validated_data)
            session.add(instance)
            session.commit()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        session = Session()
        instance = session.query(SQLAlchemyComparePairs).get(pk)
        return instance

    def get(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = ComparePair_Serializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = ComparePair_Serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            serializer = ComparePair_Serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        instance = self.get_object(pk)
        if instance:
            session = Session()
            session.delete(instance)
            session.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)