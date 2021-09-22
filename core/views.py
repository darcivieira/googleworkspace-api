from rest_framework.views import APIView, status
from rest_framework.response import Response

from .gws import Workspace
from .models import AuditLog
from .serializers import AuditLogSerializer


class UserAPIView(APIView):

    gws = Workspace

    def get(self, request):
        options = request.data
        api_options = options['api_options']

        if options.get('api_options'):
            serializer_data = options
            serializer_data['api_options'] = str(options['api_options'])
            serializer = AuditLogSerializer(data=serializer_data)
            if serializer.is_valid(raise_exception=True):
                response_data = self.gws().get_user(api_options)
                serializer.save()
                return response_data
        return Response({'error_msg': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! POST'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! PUT'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! PATCH'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)


class GroupAPIView(APIView):

    gws = Workspace

    def get(self, request):
        options = request.data
        if options.get('user_id') and options.get('access_type') == "GET" and options.get('api_options'):
            return self.gws().get_user(options['api_options'])
        return Response({'error_msg': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! POST'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! PUT'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! PATCH'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)


class DeviceAPIView(APIView):

    gws = Workspace

    def get(self, request):
        options = request.data
        if options.get('user_id') and options.get('access_type') == "GET" and options.get('api_options'):
            return self.gws().get_user(options['api_options'])
        return Response({'error_msg': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! POST'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! PUT'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! PATCH'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        options = request.data
        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)
