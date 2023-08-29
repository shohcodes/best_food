from rest_framework.filters import BaseFilterBackend


class FoodStatusFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_active = request.query_params.get('is_active')
        if is_active:
            queryset = queryset.filter(is_active=is_active)
        return queryset
