from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DataSerializer

@api_view(['POST'])
def getData(request):

    serializer = DataSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)