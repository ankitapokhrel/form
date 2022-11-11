
from rest_framework.decorators import api_view
from rest_framework.response import Response


from app.models import Form

from .serializers import FormSerializer



from django.shortcuts import get_object_or_404

from rest_framework import viewsets






class FormViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset=Form.objects.all()
    serializer_class = FormSerializer

    # serializer_class=FormSerializer 
    # queryset=Form.objects.all()
    # method=['POST']

    # def list(self, request):
    #     queryset = form.objects.all()
    #     serializer = FormSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

