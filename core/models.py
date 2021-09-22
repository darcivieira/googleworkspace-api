from django.db import models


class AuditLog(models.Model):
    created = models.DateTimeField('Data de criação', auto_now_add=True)
    user_id = models.CharField('User ID', max_length=100)
    access_type = models.CharField("Access Type", max_length=50)
    api_url = models.CharField("Url Information", max_length=50)
    api_options = models.TextField("API Options", max_length=1500)

    class Meta:
        verbose_name = 'AuditLog'
        verbose_name_plural = 'AuditLogs'
        ordering = ['id']

    def __str__(self):
        return self.created



