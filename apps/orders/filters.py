from rest_framework.filters import BaseFilterBackend


class OrderStatusFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
