from django.shortcuts import render
from django.http import HttpResponse

dummyData = [
    {
        'id': 1,
        'name': 'John',
        'city': 'New York'
    },
    {
        'id': 2,
        'name': 'Jane',
        'city': 'Los Angeles'
    },
    {
        'id': 3,
        'name': 'Mike',
        'city': 'Chicago'
    }
]


def userById(request, id):
    html = ""
    for data in dummyData:
        if data['id'] == id:
            html += f"""
            <hr>
            <h1>{data['name']}</h1>
            <p>City: {data['city']}</p>
            <hr>
            """
            break
    if not html:
        html = "<h1>User not found</h1>"
    return HttpResponse(html)

def helloWorld(request):
    return HttpResponse("Hello World!")

def allUsers(request):
    html = "<h1>User Detais: </h1>"
    for data in dummyData:
        html += f"""
        <h2>{data['name']}</h2>
        <p>City: {data['city']}</p>
        <hr>
        """
    return HttpResponse(html)