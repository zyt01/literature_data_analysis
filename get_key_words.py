#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors

def get_distinct_key_words(conn):
	get_cur = conn.cursor()
	fw = open('key_words.txt', 'w+')

	get_cur.execute("SELECT DISTINCT `word` FROM `key_words`")

	for row in get_cur:
		fw.write(row['word'].encode('utf-8'))
		fw.write('\n')
		# print(row['word'].encode('utf-8'))

	get_cur.close()
	fw.close()

def get_sum_key_words(conn, file_write):
	fw = open(file_write, 'w+')

	get_cur = conn.cursor()
	# insert_cur = conn.cursor()

	get_cur.execute("SELECT `subject_words` FROM `literature` WHERE `subject_words` != ''")
	# get_cur.execute("SELECT `subject_words` FROM `literature`")

	for row in get_cur:
		words_string =  (','.join(row.get('subject_words').split())).encode('utf-8') + '\n'
		# print words_string
		fw.write(words_string)

	get_cur.close()
	fw.close()

def get_key_words(conn):
	get_cur = conn.cursor()
	insert_cur = conn.cursor()

	get_cur.execute("SELECT `abstract_number`, `subject_words` FROM `literature`")

	print(get_cur.description)

	i = 0
	for row in get_cur:
		sql_string = ''
		subject_words = row.get('subject_words')
		abstract_number = row.get('abstract_number')
		i = i + 1
		print(i)
		if subject_words != '':
			words = subject_words.split()
			if len(words) > 0:
				for word in words:
					# print('%s %s %s' % (x, w, abstract_number))
					sql_string += "select distinct `word` FROM `key_words`;INSERT INTO `key_words` (`word`, `abstract_number`) VALUES ('%s', '%s');" % (word, abstract_number)
				insert_cur.execute(sql_string)
				conn.commit()
	get_cur.close()
	insert_cur.close()

def main():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='forestry_literature', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

	# get_distinct_key_words(conn)

	get_sum_key_words(conn, 'sum_key_words.csv')

	conn.close()

if __name__ == '__main__':
	main()
