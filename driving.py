country = input('請輸入您的國家:')
age = input('請輸入您的年齡:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照唷>.^')
	else:
		print('你還不能考駕照sorry啦 :P')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照唷>.^')
	else:
		print('你還不能考駕照sorry啦 >__<')
else:
	print('國家請輸入台灣或美國 謝謝!')

