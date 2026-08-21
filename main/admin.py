from django.contrib import admin
from django.core.mail import send_mail
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'reply')

    def save_model(self, request, obj, form, change):
        # Check if reply existed before
        old_obj = None
        if obj.pk:
            try:
                old_obj = ContactMessage.objects.get(pk=obj.pk)
            except ContactMessage.DoesNotExist:
                pass

        super().save_model(request, obj, form, change)

        # Only send email if:
        # 1. Reply exists
        # 2. Reply is NEW or changed
        if obj.reply and (not old_obj or old_obj.reply != obj.reply):
            print("🔥 SENDING EMAIL FROM ADMIN")

            send_mail(
                subject="Reply from Space Technologies",
                message=obj.reply,
                from_email=None,
                recipient_list=[obj.email],
                fail_silently=False,
            )
            