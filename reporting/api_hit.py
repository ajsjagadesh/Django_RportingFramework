from requests import get, post, put


class api_hit():
    def format_data(self,context, resp):
        if "url" in context:
            # Format the URL with data
            context['url'] = context['url'].format(**resp)
        
        if "http_headers" in context:
            context['http_headers'] = {key: value.format(**resp) if isinstance(value, str) else value for key, value in context['http_headers'].items()}
        
        if 'request_body' in context:
            context['request_body'] = {key: value.format(**resp) if isinstance(value, str) else value for key, value in context['request_body'].items()}
        print("************")
        print(context)
        print("************")
        return context


    def api_hit(self, context):
        resp = ""
        if context['http_method'] == "POST":
            if 'http_headers' in context:
                if 'request_body' in context:
                    resp = post(url=context['url'], headers=context['http_headers'], json=context['request_body'], verify=False)
                else:
                    resp = post(url=context['url'], headers=context['http_headers'], verify=False)
            else:
                if 'request_body' in context:
                    resp = post(url=context['url'], json=context['request_body'], verify=False)
                else:
                    resp = post(url=context['url'], verify=False)

        elif context["http_method"] == "PUT":
            if 'http_headers' in context:
                if 'request_body' in context:
                    resp = put(url=context['url'], headers=context['http_headers'], json=context['request_body'], verify=False)
                else:
                    resp = put(url=context['url'], headers=context['http_headers'], verify=False)
            else:
                if 'request_body' in context:
                    resp = put(url=context['url'], json=context['request_body'], verify=False)
                else:
                    resp = put(url=context['url'], verify=False)

        elif context['http_method'] == "GET":
            if 'http_headers' in context:
                if 'request_body' in context:
                    resp = get(url=context['url'], headers=context['http_headers'], json=context['request_body'], verify=False)
                else:
                    resp = get(url=context['url'], headers=context['http_headers'], verify=False)
            else:
                if 'request_body' in context:
                    resp = get(url=context['url'], json=context['request_body'], verify=False)
                else:
                    resp = get(url=context['url'], verify=False)
        return resp
    

    def error(self,resp):
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
        return context
    

api = api_hit()