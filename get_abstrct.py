#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import jieba
import jieba.analyse
import pymysql.cursors

def get_abstrct_words(conn):
	get_cur = conn.cursor()
	insert_cur = conn.cursor()

	get_cur.execute("SELECT `abstract_number`, `abstract_content` FROM `literature`")

	print(get_cur.description)

	# result = cur.fetchone()

	# print(result[1])
	i = 0
	for row in get_cur:
		sql_string = ''
		abstract_content = row.get('abstract_content')
		abstract_number = row.get('abstract_number')
		i = i + 1
		print(i)
		if abstract_content != '':
			analyseResult = jieba.analyse.extract_tags(abstract_content, topK=5, withWeight=True, allowPOS=())
			if len(analyseResult) > 0:
				for x, w in analyseResult:
					# print('%s %s %s' % (x, w, abstract_number))
					sql_string += "INSERT INTO `abstrct_key_words` (`word`, `weight`, `abstract_number`) VALUES ('%s', '%s', '%s');" % (x, w, abstract_number)
				insert_cur.execute(sql_string)
				conn.commit()
	get_cur.close()
	insert_cur.close()

def main():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='forestry_literature', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

	get_abstrct_words(conn)

	conn.close()

if __name__ == '__main__':
	main()
