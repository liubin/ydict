# coding:utf-8
import requests
from lxml import etree
import sys
import os

reload(sys)
sys.setdefaultencoding( "utf-8" )

if len(sys.argv) != 2:
	print "please use python search.py <word>"
	exit(1)

word = sys.argv[1]

url = "http://dict.youdao.com/w/eng/%s/#keyfrom=dict2.index" % word

html = requests.get(url)

doc = etree.HTML(html.text)

def pattern_1(doc):
	attr = doc.xpath('//*[@id="phrsListTab"]/div[2]')
	if len(attr) == 0:
		return ""
	# print attr
	attr = attr[0][0]

	s = ""
	for li in attr:
	    s = s + li.text
	    # print li.text

	return s


def pattern_2(doc):
	attr = doc.xpath('//*[@id="phrsListTab"]/div[1]')
	if len(attr) == 0:
		return ""
	# print attr
	attr = attr[0][0]

	s = ""
	for li in attr:
	    s = s + li.text
	    # print li.text

	return s

def download_audio(word):
	url = "http://dict.youdao.com/dictvoice?audio=%s&type=1" % word
	html = requests.get(url)
	file_name = "/tmp/%s-audio.mp3" % word
	file = open(file_name, 'wb')
	file.write(html.content)
	file.close()
	return file_name

s = pattern_1(doc)

if s == "":
	s = pattern_2(doc)

if s == "":
	print "error"
	exit(1)

print s

file = download_audio(word)
os.system("afplay %s" % file)




