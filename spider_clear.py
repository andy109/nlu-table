#!/usr/bin/env python
# coding: utf-8
import json
from bs4 import BeautifulSoup

OUT_DIR = '/storage'


def read_json():
	ll = []
	with open(OUT_DIR + 'data/modular-branches.json') as f:
		blocks = json.loads(f.read())
		for block in blocks:
			ll.append(block['name'])

	return ll


def get_html_files():
	ll = []
	for i in range(1, 4):
		with open(OUT_DIR + 'data/' + str(i) + '.html', encoding='utf8') as f:
			html_doc = f.read()
			soup = BeautifulSoup(html_doc, 'html.parser')
			results = soup.find_all('li')
			for child in results:
				a1 = child.find_all('a', class_="branch-name css-truncate-target v-align-baseline width-fit mr-2 Details-content--shown")
				ll.append(a1[0].get_text())
	return ll


l1 = read_json()
print(len(l1))
a = set(l1)
# print(a)
l2 = get_html_files()
print(len(l2))
b = set(l2)
# print(b)
print(a.intersection(b))
print(a.union(b))
print('------in a and not in b-------')
print(a.difference(b))
print('------in b and not in a-------')
print(b.difference(a))

