import functools

def login_required(func):
    f = func
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        try:
            if(args[0].session["usuario"]):
                pass
            else:
                raise Exception
        except:
            return redirect("/")
        else:
            return f(*args, **kwargs)
    return wrapper_login_required


@login_required
def home(request):
    return render(request, 'home.html')
