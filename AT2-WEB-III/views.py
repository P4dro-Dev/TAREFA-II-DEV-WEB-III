from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def post_hello(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "Guest")
            return JsonResponse({"message": f"Hello, {name}!"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "POST method required"}, status=405)