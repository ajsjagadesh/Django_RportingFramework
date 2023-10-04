from django.shortcuts import render, HttpResponse
import settings.settings_dev as s
import json
from requests import get, post, put
# Create your views here.

__author__ = 'ajagadish.nayak'


def report(req):
    context = { 
                "input": [
                    { "label": "WMS", "name": "wsn", "type":"text", "required" : "required" },
                    { "label": "Age", "name" : "age", "type":"text" },
                    # { "label": "Mobile Number", "name": "traking_id", "type":"text" },
                    { "label": "Roll Number", "name": "rollnumber", "type":"checkbox" },
                    { "label" : "Space", "name":"space", "type":"number", "min":10, "max":999  },
                    { "label" : "Select paymant mode", "name": "pay_mode", "type" : "options", "options":["Credit-Card", "Debit-Card", "UPI"]},
                    { "name":"submit","type":"submit"  }
                ],
                "report_name" :  "Get Prexo WSN Details"

            }
    return render(req, "reporting.html", context)


def form_input(req):
    resp = {}
    for key, value in req.POST.items():
        resp[key] = value
    # print(resp)
    context = {   
            "url": "http://10.24.0.15/inventory/wsn?storage_location=product_exchange_area&wsns={wsn}",
            "http_method": "GET",
            "http_headers": {
                "Content-Type": "application/json"
            }
    }

    data = format_data(context, resp)
    resp = api_hit(data)

    response = HttpResponse(f"<h1>{resp.text}</h1>", content_type="text/html")
    return response


def format_data(context, resp):
    if "url" in context:
        # Format the URL with data
        context['url'] = context['url'].format(**resp)
    
    if "http_headers" in context:
        context['http_headers'] = {key: value.format(**resp) if isinstance(value, str) else value for key, value in context['http_headers'].items()}
    
    if 'request_body' in context:
        context['request_body'] = {key: value.format(**resp) if isinstance(value, str) else value for key, value in context['request_body'].items()}
    return context


def api_hit(context):
    resp = ""
    if context['http_method'] == "POST":
        if 'request_body' in context:
            resp = post(url=context['url'], headers=context['http_headers'], json=context['request_body'])
        else:
            resp = post(url=context['url'], headers=context['http_headers'])

    elif context["http_method"] == "PUT":
        if 'request_body' in context:
            resp = put(url=context['url'], headers=context['http_headers'], json=context['request_body'])
        else:
            resp = put(url=context['url'], headers=context['http_headers'])

    elif context['http_method'] == "GET":
        if 'request_body' in context:
            resp = get(url=context['url'], headers=context['http_headers'], json=context['request_body'])
        else:
            resp = get(url=context['url'], headers=context['http_headers'])
    return resp
    