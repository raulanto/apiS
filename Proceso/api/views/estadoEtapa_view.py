from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from ..serializers import EstadoEtapaSerializer,EstadoEtapaCreateSerializer,EstadoEtapaUpdateSerializer

from Proceso.models import EstadoEtapa
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio

class EstadoEtapaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = EstadoEtapa.objects.all()

    serializer_class = EstadoEtapaSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = EstadoEtapaUpdateSerializer
        response = super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Estado Etapa actualizado"
        registrarCambio(request, objeto, mensaje)

        return response


class EstadoEtapaProductoCreateViewSet(CreateAPIView):
    queryset = EstadoEtapa.objects.all()
    serializer_class = EstadoEtapaCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Estado Etapa creado"
        registrarCambio(self.request, instance, mensaje)