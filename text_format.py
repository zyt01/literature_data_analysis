#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import quote
from urllib import unquote
import pymysql.cursors
import re

def text_format(file_read, file_write):
	fr = open(file_read, 'r')
	all_the_text = fr.read()
	fr.close()
	all_the_text = all_the_text.replace('\n', '\r\n')

	fw = open(file_write, 'w')
	
	fw.write(all_the_text)

	fw.close()

def main():
	text_format('date_literature/format/text.txt', 'date_literature/format/text.txt')
	text_format('date_literature/format/2010_1.txt', 'date_literature/format/2010_1.txt')
	
	text_format('date_literature/format/2010_2.txt', 'date_literature/format/2010_2.txt')
	text_format('date_literature/format/2010_3.txt', 'date_literature/format/2010_3.txt')
	text_format('date_literature/format/2011_1.txt', 'date_literature/format/2011_1.txt')
	text_format('date_literature/format/2011_2.txt', 'date_literature/format/2011_2.txt')
	text_format('date_literature/format/2012.txt', 'date_literature/format/2012.txt')

if __name__ == '__main__':
	main()
