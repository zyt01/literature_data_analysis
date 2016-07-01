# literature_data_analysis
literature data analysis

# File list
- text_format.py
  ```python
  python text_format.py
  ```
  整理文献数据（统一换行）

- date_literature/format
  整理后的文献数据

- connect.py
  ```python
  python connect.py
  ```
  将文献数据存入数据库

- abstract_content_update.py
  ```python
  python abstract_content_update.py
  ```
  修复数据的格式（回车）问题

- get_abstrct.py
  ```python
  python get_abstrct.py
  ```
  从文献数据的摘要中，使用 tf-idf 得到关键词和权重，存入数据库

- get_key_words.py
  ```python
  python get_key_words.py
  ```
  从文献数据中，取得关键词，存入数据库和文本

- data_forestry_literature
  sql File

- key_words.txt
  关键词列表

- sum_key_words.csv
  关键词项集
