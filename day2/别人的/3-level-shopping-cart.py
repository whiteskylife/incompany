#!/usr/bin/python3

import json

exit_flag = False #indicator to identify whether the program should exit



#shopping cart that keeps all items from user input
# 5-Tuple (product name','price','qty','total amount','datetime')
shopping_cart_list = []	#('iPhone', 5888, 1, '5888','2016-08-23 21:13:32')
product_list = []
output_list = []
shopping_cart_history = {} # outer dict
shopping_cart_dict = {}	# Inner dict: Tuple format
product_list = []

with open('product_category.json', 'r') as f:
	category = json.load(f)
	cat_keys = category.keys()

top_level_category = list(cat_keys)

top_level_tuple = []
second_level_tuple = []

while exit_flag is not True:
	# 用戶啟動程序後打印商品列表
	print("Top Level Category list".center(50,'-'))
	for item in enumerate(top_level_category): # (0, ('iphone', 5888))
		index = item[0]			
		p_name = item[1]		
		top_level = (index,p_name)
		top_level_tuple.append(top_level)
		print(index,".",p_name)

	user_choices = input("[q=quit][c=check][h=history][d=deposit] What do you want to buy?") # 允許用戶不斷的購買各種商品

	# input the item you want to buy
	if user_choices.isdigit():
		user_choices = int(user_choices)
		pass

		second_level_menu = top_level_tuple[user_choices][1] #(index,p_name)
		# print(category[second_level_menu])
		second_level_category = list(category[second_level_menu][0].keys())
		print("Second Level Category list".center(50,'-'))
		second_level_tuple.clear()

		for second_level_items in enumerate(second_level_category):
			index = second_level_items[0]
			second_level_name = second_level_items[1]
			second_level = (index,second_level_name)
			second_level_tuple.append(second_level)
			print(index,".",second_level_name) #

		second_level_user_choices = input("Next....... ")

		if second_level_user_choices.isdigit():
			second_level_user_choices = int(second_level_user_choices)

			second_level_user_menu = second_level_tuple[second_level_user_choices][1]

			length_of_third_level = len(category[second_level_menu][0][second_level_user_menu])


			third_level_loop = category[second_level_menu][0][second_level_user_menu]
			print("Third Level Category list".center(50,'-'))
			product_list.clear()

			for third_level_items in enumerate(range(length_of_third_level)):
				index = third_level_items[0]
				third_level_item_name = third_level_loop[index]["Name"]
				third_level_item_price = third_level_loop[index]["Price"]
				print(index,".",third_level_item_name,third_level_item_price)
				product = (third_level_item_name,third_level_item_price)

				product_list.append(product)
		

			third_level_user_choices = input("Which one do you want buy....... ")

			if third_level_user_choices.isdigit():
				third_level_user_choices = int(third_level_user_choices)

				if third_level_user_choices < len(product_list):
					p_item = product_list[third_level_user_choices]	# Extract the user_choice item from the Product list: ('iphone', 5888)
					exit("Thank you for purchase! Bye")
			
			else:
				print("Please input a valid choice [0 - {}]: ".format(len(product_list)))
				continue