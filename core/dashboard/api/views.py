from rest_framework import generics,views,viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from ..models import *
from .paginations import DefaultPagination

class GatewayCardReaderApiView(generics.GenericAPIView):
    serializer_class = GatewayCardReaderSerializer
    
    def post(self,request, *args,**kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        detail,code = self.process_authorization(serializer.data)
        return Response(data={"detail":detail},status=code)
    
    def process_authorization(self,data):        
        try:
            reader_gateway_obj = ReaderGateway.objects.get(gateway_id=data.get("card_reader",None))
        except:
            return "Gateway Not Found",status.HTTP_401_UNAUTHORIZED        
        EventLog.objects.create(gateway=reader_gateway_obj,card=data.get('card_id',None))
        try:
            card_obj = UIDCard.objects.get(gateway=reader_gateway_obj,card_id=data.get('card_id',None))
            if card_obj.access != 1:
                return "not authorized",status.HTTP_401_UNAUTHORIZED
            else:
                return "authorized",status.HTTP_202_ACCEPTED
        except UIDCard.DoesNotExist:
            return "not authorized",status.HTTP_401_UNAUTHORIZED
    
class CardReaderListApiView(generics.ListCreateAPIView):
    serializer_class = CardReaderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ReaderGateway.objects.filter(user=self.request.user)
    


class CardReaderDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardReaderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ReaderGateway.objects.filter(user=self.request.user)
    
class CardUidListApiView(generics.ListCreateAPIView):
    serializer_class = CardUidSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UIDCard.objects.filter(user=self.request.user)

class CardUidDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardUidSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UIDCard.objects.filter(user=self.request.user)
    
class CardReaderLogApiView(generics.ListAPIView):
    serializer_class = EventLogSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination
    
    def get_queryset(self):
        return EventLog.objects.filter(gateway__user=self.request.user)