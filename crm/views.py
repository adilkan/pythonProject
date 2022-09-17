from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .serializers import *
from .models import Client, Company, CreditSpecialist, Occupation, Property, Guarantor, TelephoneConversation, DataKK


class APIClient(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerializerClient


class APICreditSpecialist(ModelViewSet):
    queryset = CreditSpecialist.objects.all()
    serializer_class = SerializerCreditSpecialist


class APIOccupation(ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = SerializerOccupation
    permission_classes = IsAdminUser


class APICompany(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = SerializerCompany


class APIProperty(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = SerializerProperty


class APIGuarantor(ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = SerializerGuarantor


class APITelephConvers(ModelViewSet):
    queryset = TelephoneConversation.objects.all()
    fields = '__all__'


class APIMeetConvers(ModelViewSet):
    queryset = MeetConversation.objects.all()
    fields = '__all__'


class APIDataKK(ModelViewSet):
    queryset = DataKK.objects.all()
    serializer_class = SerializersDataKK
    # permission_classes = IsAdminUser
