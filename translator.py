from translate import Translator
trans = Translator(to_lang = 'ja')
try:
	with open('translator_test') as test:
		read = test.read()
		out = trans.translate(read)
		print(out)
except FileNotFoundError:
	print('file path is wrong')

with open('output.txt',mode='w') as txt:
	txt.write(out)
