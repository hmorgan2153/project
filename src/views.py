from django.shortcuts import render

def dcmain(request):
	return render(request, "dcmain.html", {})

def big_data(request):
	return render(request, "big_data.html", {})

def data_architecture(request):
	return render(request, "data_architecture.html", {})

def BI_MI(request):
	return render(request, "BI_MI.html", {})

def Master_Data(request):
	return render(request, "Master_Data.html", {})

def Data_Q(request):
	return render(request, "Data_Q.html", {})

def PSmain(request):
	return render(request, "PSmain.html", {})

def books(request):
	return render(request, "books.html", {})
