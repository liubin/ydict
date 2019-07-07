# coding:utf-8
import requests
from lxml import etree
import sys
import os

data_dir = ".dict"

if not os.path.exists(data_dir):
	os.mkdir(data_dir)

def pattern_1(doc):
	attr = doc.xpath('//*[@id="phrsListTab"]/div[2]')
	if len(attr) == 0:
		attr = doc.xpath('//*[@id="phrsListTab"]/div[1]')
		if len(attr) == 0:
			return ""

	if len(attr[0]) == "":
		return ""

	attr = attr[0][0]

	s = ""
	for li in attr:
	    s = s + li.text
	    # print li.text

	return s


def download_audio(word):
	url = "http://dict.youdao.com/dictvoice?audio=%s&type=1" % word
	html = requests.get(url)
	file_dir = "%s/%s/" % (data_dir, word)
	os.system("mkdir -p %s" % file_dir)

	file_name = "%s/audio.mp3" % file_dir
	file = open(file_name, 'wb')
	file.write(html.content)
	file.close()
	return file_name

def save_content(word, content):
	file_dir = "%s/%s/" % (data_dir, word)
	os.system("mkdir -p %s" % file_dir)
	file_name = "%s/content.txt" % file_dir
	file = open(file_name, 'wb')
	file.write(content)
	file.close()

def load_from_net(word):

	url = "http://dict.youdao.com/w/eng/%s/#keyfrom=dict2.index" % word

	html = requests.get(url)

	doc = etree.HTML(html.text)

	s = pattern_1(doc)

	if s != "":
		save_content(word, s)
		download_audio(word)
	return s

def load_from_cache(word):
	file_dir = "%s/%s/" % (data_dir, word)
	if not os.path.exists(file_dir):
		return ""
	file_name = "%s/content.txt" % file_dir
	if not os.path.exists(file_name):
		return ""
	file = open(file_name, 'r')
	s = file.read()
	file.close()
	return s

reload(sys)
sys.setdefaultencoding( "utf-8" )

if len(sys.argv) != 2:
	print "please use python search.py <word>"
	exit(1)

word = sys.argv[1]

s = load_from_cache(word)

if s == "":
	s = load_from_net(word)

if s == "":
	print "%s not found" % word
	exit(1)

print s

audio_file = "%s/%s/audio.mp3" % (data_dir, word)
os.system("afplay %s" % audio_file)
