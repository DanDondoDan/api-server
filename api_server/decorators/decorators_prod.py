from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(foo):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", ""),
        amount = args[0].request.data.get("amount", ""),
        category = args[0].request.data.get("category", ""),
        photo = args[0].request.data.get("photo", ""),
        
        if not name and not amount and not category and not photo:
            return Response(
                data={
                    "message": "required to add a product"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return foo(*args, **kwargs)
    return decorated