from django.http import JsonResponse
import requests

def fetch_public_api_list(request):
    try:
        response = requests.get('https://api.publicapis.org/entries')
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()  # Converts the response to JSON

        return JsonResponse(data)  # Return a JsonResponse object with your data
    except requests.exceptions.RequestException as e:
        # Log the error or handle it as needed
        print(e)

        # Return an empty JsonResponse or an error message in JSON format
        return JsonResponse({'error': 'An error occurred'}, status=500)