from rest_framework import generics
from . import models
from rest_framework import status
from rest_framework.response import Response
from . import serializers
from django.core.exceptions import FieldError


class NewsListView(generics.ListAPIView):
    permission_classes = ()
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

    def list(self, request, *args, **kwargs):
        order = request.query_params.get('order')
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        queryset = self.queryset.all()
        allowed_params = [field.attname for field in models.News._meta.fields]
        allowed_params += ['-{}'.format(param) for param in allowed_params]

        if order:
            if order not in allowed_params:
                return Response(
                    {
                        'message': 'invalid_param'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            queryset = queryset.order_by(order)

        if offset and limit:
            try:
                offset = int(offset)
                limit = int(limit)
                if limit < 0 or offset < 0:
                    return Response(
                        {
                            'message': 'negative limit or offset is not allowed'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except ValueError:
                return Response(
                    {
                        'message': 'invalid_param'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            queryset = queryset[offset: offset + limit]

        elif offset:
            try:
                offset = int(offset)
                if offset < 0:
                    return Response(
                        {
                            'message': 'negative offset is not allowed'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except ValueError:
                return Response(
                    {
                        'message': 'invalid_param'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            queryset = queryset[offset:offset + 5]

        elif limit:
            try:
                limit = int(limit)
                if limit < 0:
                    return Response(
                        {
                            'message': 'negative limit is not allowed'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except ValueError:
                return Response(
                    {
                        'message': 'invalid_param'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            queryset = queryset[:limit]

        serializer = self.serializer_class(queryset,
                                           many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
