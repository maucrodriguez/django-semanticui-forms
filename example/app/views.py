from django.shortcuts import render
from .forms import ManyFieldsExampleForm, ExampleModelForm, ExampleForm

# Create your views here.
def example_form(request):
	form = ExampleForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "form.html", {
		"form": form,
	})


def example_modelform(request):
	form = ExampleModelForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "modelform.html", {
		"form": form,
	})


def example_manyfieldsform(request):
	form = ManyFieldsExampleForm(request.POST or None)

	if request.POST and form.is_valid():
		pass # Do whatever

	return render(request, "manyfieldsform.html", {
		"form": form,
	})

