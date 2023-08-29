from rest_framework.filters import BaseFilterBackend


class PostStatusFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get('status')
        if status:
            if status == '1':
                queryset = queryset.filter(status='available')
            elif status == '0':
                queryset = queryset.filter(status='unavailable')
            else:
                return []
        return queryset
