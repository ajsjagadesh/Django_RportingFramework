from django.shortcuts import render
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
    
    


