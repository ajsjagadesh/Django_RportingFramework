from django.db import models

    
class CustomReportConfigManager(models.Manager):
    def get_reports_by_name(self, report_name):
        return self.filter(report_name=report_name)
    
class Custom_Report_Config(models.Model):
    id = models.AutoField(primary_key=True)
    report_name = models.CharField(max_length=200)
    input_page = models.JSONField()
    server_query = models.JSONField()
    output_page = models.JSONField()

    objects = CustomReportConfigManager()
    
    class Meta:
        # Specify the table name directly, without app name prefix
        db_table = "custom_report_config"

