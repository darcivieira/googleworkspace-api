from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .gws import Workspace
from .models import AuditLog
from .serializers import AuditLogSerializer


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class UserAPIView(APIView):

    gws = Workspace

    def get(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "GET":
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
        api_options = options['api_options']

        if options['access_type'] == "POST":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().insert_user(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! POST'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "PUT":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().update_user(api_options)
                    serializer.save()
                    return response_data

        return Response({'error_msg': 'Something went wrong! PUT'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "DELETE":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().delete_user(api_options)
                    serializer.save()
                    return response_data

        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)


class GroupAPIView(APIView):

    gws = Workspace

    def get(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "GET":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().get_group(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "POST":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().insert_group(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! POST'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "PUT":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().update_group(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! PUT'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "DELETE":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().delete_group(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)


class MemberAPIView(APIView):

    gws = Workspace

    def get(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "GET":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().get_members(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "POST":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().insert_member(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! POST'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "DELETE":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().delete_member(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)


class DeviceAPIView(APIView):

    gws = Workspace

    def get(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "GET":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().get_devices(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        options = request.data
        api_options = options['api_options']

        if options['access_type'] == "DELETE":
            if options.get('api_options'):
                serializer_data = options
                serializer_data['api_options'] = str(options['api_options'])
                serializer = AuditLogSerializer(data=serializer_data)
                if serializer.is_valid(raise_exception=True):
                    response_data = self.gws().delete_devices(api_options)
                    serializer.save()
                    return response_data
        return Response({'error_msg': 'Something went wrong! DELETE'}, status=status.HTTP_400_BAD_REQUEST)


class LogAPIView(APIView):
    pagination_class = BasicPagination
    serializer_class = AuditLogSerializer

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                                                self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request):
        instance = AuditLog.objects.all().order_by('created').reverse()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
                                                                           many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        # serializer = AuditLogSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)