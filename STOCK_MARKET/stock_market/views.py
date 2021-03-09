from django.shortcuts import render, redirect
import requests #connect to 3rd party API
import json #javascript notation, it comes back as json text
from .models import stock
from .forms import stockform
from django.contrib import messages


# Create your views here.

def home(request):
	
	if request.method == "POST":
		ticker = request.POST["ticker"]
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_31a6f56345a6414ebe439630100bab82")
		
		try:
			api= json.loads(api_request.content)
			
		except Exception as e:
			api = "Error, 404 No found"
		
		return render(request,'home.html',{"api":api})
	
	else:
		return render(request,'home.html',{"ticker":"Enter a ticker "})
	


def about(request):
	return render(request,'about.html',{})
		
def add_stock(request):

	if request.method == "POST":
		form = stockform(request.POST or None)
		
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect("add_stock")
		
	else:
		ticker = stock.objects.all()
		output = []
		for ticker_item in ticker:
		
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_31a6f56345a6414ebe439630100bab82")
			
			try:
				api= json.loads(api_request.content)
				output.append(api)
				
				
			except Exception as e:
				api = "Error, 404 No found"
		
		return render(request, 'add_stock.html', {"ticker":ticker, "output":output} )
		
		
def delete(request, stock_id):
	item = stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted"))
	return redirect(delete_stock) 
	

def delete_stock(request):
	ticker = stock.objects.all()
	return render(request,'Delete_Stock.html',{'ticker': ticker})

	
