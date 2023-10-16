from django.shortcuts import render, HttpResponse
import settings.settings_dev as s
import json
from requests import get, post, put
from reporting.models import Custom_Report_Config
from . api_hit import api
import pandas as pd
from django.http import HttpResponse
import uuid

# Create your views here.



__author__ = 'ajagadish.nayak'

_report_name = ''
final_report_name = ''
final_data = ''
report_title = ''

def report_home(req):
    all_report = Custom_Report_Config.objects.all()
    reports_name = []
    for reports in all_report:
        reports_name.append(reports.report_name)
    # print("*******************************************")
    # print(reports_name)
    # print("*******************************************")
    context = {
        "report_name" : reports_name 
    }
    # print(context)
    return render(req, "report_home.html", context)


def report(req):
    report_name = req.POST.get("report_name")
    # print(report_name)
    global _report_name, final_report_name
    _report_name = report_name
    report = Custom_Report_Config.objects.get_reports_by_name(report_name)
    # report = get_report_data(report_name)
    for input in report:
        context = input.input_page
    final_report_name = context['report_name']
    print(context)
    return render(req, "reporting.html", context)


def report_procces(req):
    resp = {}
    for key, value in req.POST.items():
        resp[key] = value
    global report_title
    if bool(resp):
        report_title = next(iter(resp.values()))
    else:
        report_title = "report"


    global _report_name
    print(_report_name)
    report = Custom_Report_Config.objects.get_reports_by_name(_report_name)
    li = []
    for server in report:
        li.append(server.server_query)
        # print(server.server_query)

    print(li)
    context = li[0]
    data = api.format_data(context, resp)
    resp = api.api_hit(data)
    # print(resp.json())
    if resp.status_code >= 200 and resp.status_code<300:
        context = output(resp)
        # print(context['row_data'])
        # print(context)
        return render(req, "table.html", context)
    context = api.error(resp)
    return render(req, "table.html", context)


def output(resp):
    global _report_name
    report = Custom_Report_Config.objects.get_reports_by_name(_report_name)
    for server in report:
        output = server.output_page
    print(output)

    if 'get' in output[0]['output'] and len(output[0]['output']['get']) > 0 :
        keys = output[0]['output']['get'].split(".")
        result = resp.json()
        for key in keys:
            if key.isdigit():
                key = int(key)
            result = result[key]
        if isinstance(result, dict):
            result = [result]
            context = row_proccese(result, output)
        elif isinstance(result, list):
            context = row_proccese(result, output)
    else :
        resp = resp.json()
        if isinstance(resp, dict):
            resp = [resp]
            context = row_proccese(resp, output)
        elif isinstance(resp, list):
            context = row_proccese(resp, output)
        context = row_proccese(resp, output)
    return context
    
def row_proccese(resp, output):
    heading = []
    keys = []
    for i in output[0]["output"]["data"]:
        heading.append(i[0])
        keys.append(i[1])

    json_data = []
    for i in resp:
        data = {}
        for k in keys:
            data[k] = str(i[k])
        json_data.append(data)
    
    global final_report_name, report_title

    if len(json_data) > 2000:
        global final_data 
        final_data = json_data
        context = {
        "Headings" : heading,
        "keys" : keys,
        "row_data" : json_data[:2000],
        "file" : "True",
        "data_len" : len(json_data),
        "link_name" : "download",
        "Report_name" : final_report_name,
        "file_name" : report_title
        }
        # print(context)
        return context
        
    context = {
        "Headings" : heading,
        "keys" : keys,
        "row_data" : json_data,
        "Report_name" : final_report_name,
         "file_name" : report_title
    }
    return context


def download(req):
    global final_data 
    df = pd.DataFrame(final_data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{uuid.uuid4()}.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response
