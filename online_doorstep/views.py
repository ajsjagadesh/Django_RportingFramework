from django.shortcuts import render, HttpResponse
from requests import get, post
import settings.settings_dev as s
import json
# Create your views here.

__author__ = 'ajagadish.nayak'

def get_traking_id(req):
    return render(req, 'form.html')

def doorstep(req):
    traking_id = req.GET.get("tracking_id")
    order_id = req.GET.get("order_id")
    order_item_unit_id = req.GET.get("order_item_unit_id")

    # print(traking_id, order_id, order_item_unit_id)
    url = ""
    if traking_id != '':
        url = str(s.API[0]['doorstep_url']) +"tracking_id=" + str(traking_id)
        print(f"URL: {url}")
    elif order_id != '':
        url = str(s.API[0]['doorstep_url']) +"order_id=" + str(order_id)
        print(f"URL: {url}")
    elif order_item_unit_id != '':
        url = str(s.API[0]['doorstep_url']) +"order_item_unit_id=" + str(order_item_unit_id)
        print(f"URL: {url}")

    fe_header = s.API[0]['fe_header']
    tl_header = s.API[0]['tl_header']
    
    fe_resp = get(url=url, headers=fe_header)
    tl_resp = get(url=url, headers=tl_header)

    json_data = []
    if len(fe_resp.json()) != 0 :
        for i in fe_resp.json()[0]['assessment_details']['assessment_checks']:
            data = {
                "question_id" : str(i['question_id']),
                "description" : str(i['description']),
                "fe_ans" : str(i['answers'][0]['value']),
                "tl_ans" : ""
            }
            json_data.append(data)

    if len(tl_resp.json()) != 0 :
        for i in tl_resp.json()[0]['assessment_details']['assessment_checks']:
            data = {
                "question_id" : str(i['question_id']),
                "description" : str(i['description']),
                "fe_ans" : "",
                "tl_ans" : str(i['answers'][0]['value']),
            }
            json_data.append(data)

    json_data = json.dumps(json_data, indent=4)
    # print(json_data)

    if len(fe_resp.json()) != 0 or len(tl_resp.json()) != 0:
        context = {
            "data" : json_data,
            "traking_id" : fe_resp.json()[0]['tracking_id'],
            "order_id" : fe_resp.json()[0]['order_id'],
            "order_item_unit_id" : fe_resp.json()[0]['order_item_unit_id'],
            "grade" : fe_resp.json()[0]['resolved_product_details']['grade']
        }
    else:
        context = {}
    return render(req, "doorstep.html", context)


def get_imei(req):
    context = { 
                "input": [
                    { "label": "IMEI", "name": "imei", "type":"text", "required" : "required" },
                    # { "label": "Age", "name" : "age", "type":"text" },
                    # { "label": "Mobile Number", "name": "traking_id", "type":"text" },
                    # { "label": "Roll Number", "name": "rollnumber", "type":"checkbox" },
                    # { "label" : "Space", "name":"space", "type":"number", "min":10, "max":999  },
                    # { "label" : "Select paymant mode", "name": "pay_mode", "type" : "options", "options":["Credit-Card", "Debit-Card", "UPI"]},
                    { "name":"submit","type":"submit"  }
                ],
                "report_name" :  "IMEI Details"

            }
    return render(req, "getIMEI.html", context)


def imei(req):
    print("*************************#####*********************************")
    resp = {}
    for key, value in req.POST.items():
        resp[key] = value
    # print(resp)
    context = {   
            "url" : "https://fkdapi.gadgetwood.com/API/flipkart/GetAssessmentByImei",
            "http_method" : "POST",
            "http_headers" : {
                "Accept":"application/json",
                "Authorization":"Bearer TtgnNAthucvK-jCX_zEQ2wpFbeTxda9KbyKw-8Biki4SJ8DjgglmZs3qhsy3ChgL5AhIl7XxKWMSf6wsxrrlRwPijI75ieWF5hUGrQYjMmaBz7qJMem0ltcjQpR3iNFrSSH7sVWzGh0M1CUWoltu5bQNo6Zri-ODbKJyCii0-801JcC-pV6LgkDhA5DvYii87UIEpn7QsuMH4mCXMWnJ2E68r7DwNQkVFt-OByR0mb0",
                "Content-Type":"application/json"
            },
            "request_body": {
                "Imei":'{imei}'
            }
    }

    data = format_data(context, resp)
    resp = post(url=data['url'], headers=data['http_headers'], json=data['request_body'], verify=False)

    # response = HttpResponse(f"<h1>{resp.text}</h1>", content_type="text/html")
    # print(resp.json()[0])
    # print("******************************************************************************")
    if resp.status_code >= 200 and resp.status_code<300:
        data = resp.json()[0]
        return render(req, "imei.html", data)
    context = error(resp)
    return render(req, "table.html", context)

    # data = resp.json()[0]
    # return render(req, "imei.html", data)


def format_data(context, resp):
    if "url" in context:
        # Format the URL with data
        context['url'] = context['url'].format(**resp)
    
    if "http_headers" in context:
        context['http_headers'] = {key: value.format(**resp) if isinstance(value, str) else value for key, value in context['http_headers'].items()}
    
    if 'request_body' in context:
        context['request_body'] = {key: value.format(**resp) if isinstance(value, str) else value for key, value in context['request_body'].items()}
    return context


def error(resp):
    heading = ["Message", "Status_Code"]
    keys = ["Message", "Status_Code"]
    mesg = [{
        "Message": str(resp.json()),
        "Status_Code": str(resp.status_code)
        }]
    context = {
        "Headings" : heading,
        "keys" : keys,
        "row_data" : mesg
    }
    print(heading)  
    print(keys)
    print(mesg)
    return context
    


