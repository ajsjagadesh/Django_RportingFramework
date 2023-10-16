import json
from reporting.models import Custom_Report_Config
# Create your views here.


report_name = ''
input_page = ''
server_query = ''
output_page = ''

def get_report_data(reports_name):
    report = Custom_Report_Config.objects.get_reports_by_name(reports_name)
    for input in report:
        report_name = input.report_name
        input_page = input.input_page
        server_query = input.server_query
        output_page = input.output_page
    
