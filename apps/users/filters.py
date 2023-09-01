from rest_framework.filters import BaseFilterBackend


class UserRoleFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        role = request.query_params.get('role')
        if role:
            queryset = queryset.filter(role=role)
        return queryset


class TelegramUserIsVerifiedFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_verified = request.query_params.get('is_verified')
        if is_verified:
            queryset = queryset.filter(is_verified=is_verified)
        return queryset


class TelegramUserIsBlockedFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_blocked = request.query_params.get('is_blocked')
        if is_blocked:
            if is_blocked == '1':
                queryset = queryset.filter(is_blocked=True)
            elif is_blocked == '0':
                queryset = queryset.filter(is_blocked=False)
        return queryset
