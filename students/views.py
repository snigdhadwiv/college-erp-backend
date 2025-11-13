from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def student_list(request):
    return Response({'message': 'Students endpoint working'})