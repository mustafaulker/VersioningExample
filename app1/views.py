from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class indexView(APIView):

    @extend_schema(responses={200: {"description": "Success"}})
    def get(self, request, version):
        if version == 'v1':
            return Response(data={'msg': 'v1'}, status=status.HTTP_200_OK)
        return Response(data={'msg': 'v3'}, status=status.HTTP_200_OK)
