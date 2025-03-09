from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response=exception_handler(exc, context)
    if response is not None:
        response.data['status_code']=response.status_code
        
    if 'detail' in response.data:
        response.data['message']=response.data.pop('detail')
    
    return response

