import traceback
try:
	value = 8 / b
	print(value)
except:
    info = traceback.extract_stack()
    print('error:',info)
else:
	print('no error')
finally:
	print('-'*100)
