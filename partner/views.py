from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # print(username, email, password)

        user = User.objects.create_user(username, email, password)
        # Article.objects.create(title="", content="")

    ctx = {}
    return render(request, "signup.html", ctx)
