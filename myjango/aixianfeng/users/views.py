from django.shortcuts import render, HttpResponse
import logging


# Create your views here.

def test_log(request):
	try:
		lists = [1, 2, 4, 5, 6, 7]
		open('aa.txt', 'r')
	except Exception as err:
		print(err)
		logging.error(err)
	return HttpResponse("哈哈。。。。")
