# _*_coding:utf-8_*_
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from App.models import AXFUser
from django.shortcuts import render, HttpResponse, redirect, reverse

# JSON请求的路径列表
LOGIN_JSON_PATH = [
	'/app/addCart/',
	'/app/changecartstate/',
	'/app/subshopping/',
	'/app/addshopping/',
	'/app/allselect/',
	'/app/unallselect/',
	'/app/payed/',
]
# 普通request请求的路径列表
LOGIN_PATH = [
	'/app/cart/',
	'/app/makeorder/',
	'/app/ordernotpay/',
]


class LoginMiddleWare(MiddlewareMixin):
	def process_request(self, request):
		print(request.path)
		if request.path in LOGIN_JSON_PATH:
			# goods_id = request.GET.get('gid')
			print("---->process_request")
			username = request.session.get('username', "")
			if username:
				# 登录
				user = AXFUser.objects.filter(username=username)
				if user.exists():
					request.user = user.first()
				else:
					return JsonResponse({'status': 'fail', 'msg': '用户不存在'})

			else:
				# 未登录
				return JsonResponse({'status': 'fail', 'msg': '用户没有登录'})

		if request.path in LOGIN_PATH:
			username = request.session.get('username', "")
			if username:
				# 登录
				user = AXFUser.objects.filter(username=username)
				if user.exists():
					request.user = user.first()
				else:
					return redirect(reverse('App:user_login'))

			else:
				# 未登录
				return redirect(reverse('App:user_login'))
