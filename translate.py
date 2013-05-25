#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Vital Kolas'
__email__ = 'ffoxin@gmail.com'
__credits__ = ['3ds@habrahabr']
__version__ = '0.1'
__date__ = '2013-05-24'

import sys
import re
import urllib
import urllib2
import json
import codecs
import string

def translate(lang_from, lang_to, word):

	url = 'http://translate.google.com/translate_a/t?%s'

	list_of_params = {
		'client' 	: 't',
		'hl' 		: 'en',
		'multires' 	: '1',
		'sl'		: lang_from,
		'tl' 		: lang_to,
		'text' 		: word
	}

	request = urllib2.Request(
		url % urllib.urlencode(list_of_params),
		headers = {
			'User-Agent': 'Mozilla/5.0',
			'Accept-Charset': 'utf-8'
		})
	res = urllib2.urlopen(request).read()

	fixed_json = re.sub(r',{2,}', ',', res).replace(',]', ']')
	data = json.loads(fixed_json)

	return data[0][0][0]

def main():
	comment = '//'

	if len(sys.argv) == 4:
		with open(sys.argv[3], 'r') as file:
			out = ''
			for line in file:
				pos = line.find(comment)
				if pos != -1:
					pos += len(comment)
					while line[pos] is ' ':
						pos += 1
					pre = line[:pos]
					src = line[pos:]
					tr = translate(sys.argv[1], sys.argv[2], src)
					out += pre + tr + '\n'
					print(src)
				else:
					out += line
		with open('out_' + sys.argv[3], 'w') as file:
			file.write(out.encode('utf8'))

if __name__ == '__main__':
	main()

