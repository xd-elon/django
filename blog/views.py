from django.shortcuts import render

# Create your views here.
def blog(request):
  # return HttpResponse("Home")
  return render(
    request,
    'home.html'
  )


# Create your views here.
def example(request):
  # return HttpResponse("Home")
  return render(
    request,
    'home.html'
  )