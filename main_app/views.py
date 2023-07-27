from django.shortcuts import render

# Create your views here.

dogs = [
  {'name': 'Bubbles', 'breed': 'French', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def dogs_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })
