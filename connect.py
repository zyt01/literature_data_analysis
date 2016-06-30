#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import quote
# from urllib import unquote
import pymysql.cursors
import re


def match_string(restring, str):
	pm = re.compile(restring)
	match = re.search(pm, str)
	if match:
		return match.group(1)
	else:
		return ''

def get_data_information(str, conn):
	str = str.replace("'", "’")
	str = str.replace('"', '“')
	print quote(str)

	abstract_number = match_string('【文摘号】([^\r]+)\r', str)
	literature_type = match_string('【文献类型】([^\r]+)\r', str)
	literature_title = match_string('【文献题名】([^\r]+)\r', str)
	responsible_person = match_string('【责任者】([^\r]+)\r', str)
	person_unit = match_string('【着者单位】([^\r]+)\r', str)
	parent_literature = match_string('【母体文献】([^\r]+)\r', str)
	volume_period = match_string('【年卷期】([^\r]+)\r', str)
	page_number = match_string('【页码】([^\r]+)\r', str)
	year = match_string('【年份】([^\r]+)\r', str)
	holding_information = match_string('【馆藏信息】([^\r]+)\r', str)
	classification_number = match_string('【分类号】([^\r]+)\r', str)
	subject_words = match_string('【主题词】([^\r]+)\r', str)
	abstract_content = match_string('【文摘内容】([^\r]+)\r', str)

	# print abstract_content

	cur = conn.cursor()

	sql_string = "INSERT INTO `literature` (`abstract_number`, `literature_type`, `literature_title`, `responsible_person`, `person_unit`, `parent_literature`, `volume_period`, `page_number`, `year`, `holding_information`, `classification_number`, `subject_words`, `abstract_content`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (abstract_number, literature_type, literature_title, responsible_person, person_unit, parent_literature, volume_period, page_number, year, holding_information, classification_number, subject_words, abstract_content)

	print sql_string

	cur.execute(sql_string)

	conn.commit()

	cur.close()

def open_file(file_string, conn):
	fd = open(file_string, 'r')
	all_the_text = fd.read()
	# print quote(all_the_text)
	text_arr = all_the_text.split('\n\r\n')
	print len(text_arr)

	for text in text_arr:
		get_data_information(text, conn)

def main():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='forestry_literature', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

	# open_file('date_literature/format/text.txt', conn)
	open_file('date_literature/format/2010_1.txt', conn)
	open_file('date_literature/format/2010_2.txt', conn)
	open_file('date_literature/format/2010_3.txt', conn)
	open_file('date_literature/format/2011_1.txt', conn)
	open_file('date_literature/format/2011_2.txt', conn)
	open_file('date_literature/format/2012.txt', conn)

	conn.close()

if __name__ == '__main__':
	main()
