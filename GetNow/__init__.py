import logging

import azure.functions as func

"""
@api [get] /api/GetNow
description: "Get the current time"
parameters:
- (query) name {String} some name to show
responses:
  200:
    description: Normal response
    content:
        text/plain:
            schema: 
                type: string
                example: some text
"""

"""
@api [post] /api/GetNow
description: "Get the current time"
parameters:
- (body) name* {String} Name can be specified in the body
- (body) param1 {String} param1 is optional, because without star
responses:
  200:
    description: Normal response
    content:
        text/plain:
            schema: 
                type: string
                example: some text
"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, ! {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
