from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat, Toy
from .forms import FeedingForm
# views.py

# Add this cats list below the imports
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  id_list = cat.toys.all().values_list('id')
  toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have})

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']
  # Special string pattern Django will use
  # success_url = '/cats/{cat_id}' <- what it may look like under hood
  # Or if you wanted to redirect to the index page
  # success_url = '/cats'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

...

# add this new function below cats_detail
def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

def assoc_toy(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Cat.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('detail', cat_id=cat_id)




