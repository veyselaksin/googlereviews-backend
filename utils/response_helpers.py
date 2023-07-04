from rest_framework.response import Response

def SuccessResponse(status, data=None, message=""):
    return Response({ 'success':True, 'data':data, 'message':message},status=status)

def ErrorResponse(status, message="", data=None):
    return Response({ 'success':False, 'data':data, 'message':message},status=status)
