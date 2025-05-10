from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# For /home/
def helloWorld(request):
    print(reverse('home'))
    return HttpResponse("Hello World!")

# For user profile related views
dummyData = [
    {
        'id': 1,
        'name': 'john',
        'city': 'New York'
    },
    {
        'id': 2,
        'name': 'jane',
        'city': 'Los Angeles',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
        'id': 3,
        'name': 'Mike',
        'city': 'Chicago'
    }
]


def userById(request, id):
    html = ""
    validId = False
    for data in dummyData:
        if data['id'] == id:
            return render(request, 'second/user_profile.html', {
                'name': data['name'],
                'city': data['city'],
            })
    return HttpResponseNotFound("User not found")
            # validId = True
            # html += f"""
            # <hr>
            # <h1>{data['name']}</h1>
            # <p>City: {data['city']}</p>
            # <hr>
            # """
            # break
    # if not validId:
    #     return HttpResponseNotFound("User not found")
    # return HttpResponse(html)

def redirectToUser(request, id):
    url = reverse('user-profile', kwargs={'id': id})
    return HttpResponseRedirect(url)

def allUsers(request):
        return render(request, 'second/all_users.html', {
            'users': dummyData,
        })

        # html += f"""
        # <h2>{data['name']}</h2>
        # <p>City: {data['city']}</p>
        # <a href="/second/all-users/redirect-to-{data['id']}" target="_blank">Visit their profile</a>

        # <hr>
        # """

# def redirectToGoogle(request, id):
#     return HttpResponseRedirect(f"/second/user/{id}/")

# def userName(request, id): 
#     html = ""
#     validId = False
#     for data in dummyData:
#         if data['id'] == id:
#             validId = True
#             html += f"Name is: {data['name']}"
#     return HttpResponse(html) if validId else HttpResponseNotFound("User not found")