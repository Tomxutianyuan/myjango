import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.template import loader

from aixianfeng.settings import DEFAULT_FROM_EMAIL
from .models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, MainFoodTypes, Goods, AXFUser, Cart, Order, \
	OrderGoods
from .app_constants import *
from .forms import UserRegisterForm, UserLoginForm


# Create your views here.

def index(request):
	wheels = MainWheel.objects.all()
	# 查询导航数据
	navs = MainNav.objects.all()
	# 查询每日必买
	mustbuys = MainMustBuy.objects.all()
	# 商店信息
	shop_goods = MainShop.objects.all()
	shop_goods_1 = shop_goods[0:1]
	print(shop_goods_1)
	shop_goods_1_3 = shop_goods[1:3]
	shop_goods_3_7 = shop_goods[3:7]
	shop_goods_7_11 = shop_goods[7:11]

	# 获取商品信息
	mainshows = MainShow.objects.all()

	return render(request, 'main/home.html',
				  {'wheels': wheels, 'title': '首页', 'navs': navs, 'mustbuys': mustbuys, 'shop_goods_1': shop_goods_1,
				   'shop_goods_1_3': shop_goods_1_3, 'shop_goods_3_7': shop_goods_3_7,
				   'shop_goods_7_11': shop_goods_7_11, 'mainshows': mainshows})


def show_market(request):
	# 接收typeid
	typeid = request.GET.get('typeid', '103541')
	childid = request.GET.get('childid', '0')
	# 排序规则
	rule_sort = request.GET.get('sort', '0')

	foodtypes = MainFoodTypes.objects.all()
	foodtype_childname_list = []

	# 定义排序规则列表
	order_list = [
		["综合排序", ORDER_TOTAL],
		["价格升序", ORDER_PRICE_UP],
		["价格降序", ORDER_PRICE_DOWN],
		["销量升序", ORDER_SALE_UP],
		["销量降序", ORDER_SALE_DOWN]
	]

	if typeid:
		# Goods.objects.all()
		goods_list = Goods.objects.filter(categoryid=typeid)
		# 判断childid是否是0，如果是0则表示全部分类，全部分类就不做任何操作
		if childid == ALL_TYPE:
			pass
		else:
			# 如果有分类则在现有的大类别中筛选childid
			goods_list = goods_list.filter(childcid=childid)

		# 排序的规则
		if rule_sort == ORDER_TOTAL:
			pass
		elif rule_sort == ORDER_PRICE_UP:
			goods_list = goods_list.order_by('price')
		elif rule_sort == ORDER_PRICE_DOWN:
			goods_list = goods_list.order_by('-price')
		elif rule_sort == ORDER_SALE_UP:
			goods_list = goods_list.order_by('productnum')
		elif rule_sort == ORDER_SALE_DOWN:
			goods_list = goods_list.order_by('-productnum')

		# 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540

		# 得到foodtype对象
		foodtype = MainFoodTypes.objects.get(typeid=typeid)
		# foodtype.childtypenames字段的值 ---》 字符串
		foodtypechildnames = foodtype.childtypenames
		# 使用split切割  ['全部分类:0','牛奶：675853'，。。。。]
		foodtypechildnames_list = foodtypechildnames.split('#')
		# 对'牛奶：675853' ---》 [['牛奶','67988'],['酸奶','9898'],[]]
		for childname in foodtypechildnames_list:
			foodtype_childname_list.append(childname.split(':'))
		print("--->", int(typeid))
	return render(request, 'main/market.html', {'foodtypes': foodtypes, 'goods_list': goods_list,
												'foodtype_childname_list': foodtype_childname_list,
												'typeid': int(typeid), 'childid': childid, 'order_list': order_list,
												"rule_sort": rule_sort})


# 定义我的
def show_mine(request):
	username = request.session.get('username', '')
	if username:
		user = AXFUser.objects.filter(username=username).first()
		not_pay_num = Order.objects.filter(o_user=user).filter(o_status=ORDER_NOT_PAY).count()
		not_receive_num = Order.objects.filter(o_user=user).filter(o_status=ORDER_NOT_RECEIVE).count()
		return render(request, 'main/mine.html',
					  {'user': user, 'not_pay_num': not_pay_num, 'not_receive_num': not_receive_num})
	else:
		return render(request, 'main/mine.html', {'user': ''})


# return render(request, 'main/mine.html',)


# 用户登录
def user_login(request):
	if request.method == 'GET':

		return render(request, 'user/login.html', {'title': '登录'})
	else:
		user_login_form = UserLoginForm(request.POST)
		if user_login_form.is_valid():
			username = user_login_form.cleaned_data['username']
			password = user_login_form.cleaned_data['password']
			# 查询用户
			user = AXFUser.objects.filter(username=username)
			if user.exists():
				user = user.first()
				if user.is_active:
					# 验证密码  password
					if check_password(password, user.password):
						# 添加到session中
						request.session['username'] = username
						return redirect(reverse('App:show_mine'))
					else:
						return render(request, 'user/login.html', {'title': '登录', 'msg': '密码不正确'})
				else:
					print('没有激活')
					return render(request, 'user/login.html', {'title': '登录', 'msg': '用户还没有激活，赶快去邮箱激活'})
			else:
				return render(request, 'user/login.html', {'title': '登录', 'msg': '没有此用户'})
		else:
			return render(request, 'user/login.html', {'title': '登录', 'user_login_form': user_login_form})


def user_register(request):
	if request.method == 'GET':
		return render(request, 'user/register.html', {'title': '注册'})
	else:
		user_register_form = UserRegisterForm(request.POST, request.FILES)
		if user_register_form.is_valid():
			print(user_register_form.cleaned_data)
			datas = user_register_form.cleaned_data
			if datas['password'] == datas['repassword']:
				user = AXFUser()
				user.username = datas['username']
				password = datas['password']
				# 加密
				password = make_password(password)
				user.password = password
				user.email = datas['email']
				user.uicon = datas['uicon']
				user.save()

				# 发送邮件
				# message = '<a href="#">激活</a>'
				u_token = uuid.uuid4().hex
				# 设置u_token和用户名进行绑定  ---》缓存到redis数据库
				cache.set(u_token, user.username, timeout=60 * 60 * 24)

				print("u_token", u_token)  # 27fd7800-670e-4c78-b818-9bc4dfb061d7
				data = {
					'username': user.username,
					'active_url': 'http://127.0.0.1:8000/app/active',
					'u_token': u_token  # 27fd7800670e4c78b8189bc4dfb061d7
				}
				message = loader.get_template('user/active.html').render(data)

				send_mail('爱鲜蜂用户激活', message, DEFAULT_FROM_EMAIL, [user.email, ], html_message=message)

				return redirect(reverse('App:user_login'))

			else:
				return render(request, 'user/register.html', {'title': '注册', "msg": '密码不一致'})

			return HttpResponse('OK')
		else:
			return render(request, 'user/register.html', {'user_register_form': user_register_form})


# ajax用于检查用户名的
def check_username(request):
	username = request.GET.get('username')
	print('username:', username)
	result = AXFUser.objects.filter(username=username)

	if result.exists():
		return JsonResponse({'status': 'fail', 'msg': '用户名已存在'})
	else:
		return JsonResponse({'status': 'ok', 'msg': '用户名可用'})


# 用户激活：
def user_active(request):
	u_token = request.GET.get('u_token')
	# 去redis缓存中取出u_token
	value = cache.get(u_token)
	# 查询用户
	user = AXFUser.objects.filter(username=value).first()
	# 修改用户激活字段
	user.is_active = True
	user.save()

	return redirect(reverse('App:user_login'))


# 退出
def user_logout(request):
	request.session.flush()
	return redirect(reverse('App:show_mine'))


# 购物车函数
def show_cart(request):
	cart_goods = Cart.objects.filter(user=request.user)
	total_price = get_totalprice(request)
	print("total_price：", total_price)
	return render(request, 'main/cart.html', {"cart_goods": cart_goods, 'total_price': total_price})


# 添加购物车操作
def add_cart(request):
	gid = request.GET.get('gid', '')

	carts = Cart.objects.filter(user_id=request.user.id).filter(goods_id=gid)
	if carts.exists():
		cart = carts.first()
		cart.goods_num = cart.goods_num + 1
	else:
		cart = Cart()
		goods = Goods.objects.get(pk=gid)
		cart.goods = goods
		cart.user = request.user
	cart.save()
	datas = {
		"status": 'ok',
		'goods_num': cart.goods_num
	}
	print(datas)
	return JsonResponse(datas)


# 定义一个方法求商品的总价
def get_totalprice(request):
	carts = Cart.objects.filter(user=request.user).filter(is_select=True)
	total_price = 0
	for goods in carts:
		price = goods.goods.price
		num = goods.goods_num
		t_price = price * num
		total_price += t_price
	return total_price


# 改变购物车商品的选中状态
def change_cart_state(request):
	cartid = request.GET.get('cartid')
	cart = Cart.objects.get(pk=cartid)
	cart.is_select = not cart.is_select
	cart.save()
	return JsonResponse({'status': 'ok', 'is_select': cart.is_select, 'total_price': get_totalprice(request)})


# 购物车界面的商品的减少
def sub_shopping(request):
	cartid = request.GET.get('cartid')
	cart = Cart.objects.get(pk=cartid)
	datas = {}
	if cart.goods_num > 1:
		cart.goods_num = cart.goods_num - 1
		cart.save()
		datas['cart_goods_num'] = cart.goods_num
	else:
		cart.delete()
		datas['cart_goods_num'] = 0

	datas['status'] = 'ok'
	datas['total_price'] = get_totalprice(request)
	return JsonResponse(datas)


# 购物车页面添加商品
def add_shopping(request):
	cartid = request.GET.get('cartid')
	cart = Cart.objects.get(pk=cartid)
	if cart:
		cart.goods_num = cart.goods_num + 1
		cart.save()
		return JsonResponse({'status': 'ok', 'cart_goods_num': cart.goods_num, 'total_price': get_totalprice(request)})


# 购物车商品的全选操作
def all_select(request):
	carts = Cart.objects.filter(user=request.user).filter(is_select=False)
	for cart in carts:
		cart.is_select = not cart.is_select
		cart.save()
	return JsonResponse({'status': 'ok', 'total_price': get_totalprice(request)})


# 购物车商品的取消全选操作
def unall_select(request):
	carts = Cart.objects.filter(user=request.user).filter(is_select=True)
	print(carts)
	for cart in carts:
		cart.is_select = not cart.is_select
		cart.save()
	return JsonResponse({'status': 'ok', 'total_price': get_totalprice(request)})


# 下单
def make_order(request):
	carts = Cart.objects.filter(user=request.user).filter(is_select=True)
	order = Order()
	order.o_user = request.user
	order.o_price = get_totalprice(request)
	order.save()

	# 向订单商品表中添加商品
	for cart in carts:
		ordergoods = OrderGoods()
		ordergoods.o_order = order
		ordergoods.o_goods = cart.goods
		ordergoods.o_goods_num = cart.goods_num
		ordergoods.save()
		# 从购物车中删除该商品
		cart.delete()

	return render(request, 'order/order_detail.html', {'order': order})


# 展示未支付的订单们
def order_notpay(request):
	orders = Order.objects.filter(o_user=request.user).filter(o_status=ORDER_NOT_PAY)
	return render(request, 'order/order_not_pay.html', {'orders': orders})


# 订单支付功能
def order_payed(request):
	orderid = request.GET.get('orderid')
	if orderid:
		order = Order.objects.get(pk=orderid)
		order.o_status = ORDER_NOT_SEND
		order.save()
		return JsonResponse({'status': 'ok'})
	else:
		return JsonResponse({'status': 'fail'})


# 未支付页面的支付动作
def order_payedother(request):
	orderid = request.GET.get('orderid')
	if orderid:
		order = Order.objects.get(pk=orderid)
		order.o_status = ORDER_NOT_RECEIVE
		order.save()
		return redirect(reverse('App:show_mine'))
