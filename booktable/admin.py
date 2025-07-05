from django.contrib import admin
from .models import UserProfile
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Booking)
class bookingAdmin(SummernoteModelAdmin):
    list_display = ('user', 'table_size', 'booking_date', 'booking_time') # Displayed columns in the admin list view
    list_filter = ('user', 'booking_date') # Filters for the admin list view
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name') # Search fields in the admin list view, Django uses __ (double underscores) in search_fields, filter, order_by, etc., to access related model fields via relationships like ForeignKey
    ordering = ('-booking_date', '-booking_time')
    summernote_fields = ('allergies',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    ordering = ('user__username',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
