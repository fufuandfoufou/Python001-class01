# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-07-17   19:25
# 文件名称    : translate  PY
# 开发工具    : PyCharm

import pymysql
import pandas as pd
import numpy as np

# 将下列sql语句改写成pandas语句
1. SELECT * FROM data;
    data[:]


2. SELECT * FROM data LIMIT 10;
    data[0:9]


3. SELECT id FROM data;  //id 是 data 表的特定一列
    data['id']

4. SELECT COUNT(id) FROM data;
    data.count('id')


5. SELECT * FROM data WHERE id<1000 AND age>30;
    data[df.id < 1000 and df.age > 30]

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
    data.groupby('id')
    data.groupby('order_id').sum()


7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    data.merge(t1, t2, on='id')

8. SELECT * FROM table1 UNION SELECT * FROM table2;
    data.concat(table2)

9. DELETE FROM table1 WHERE id=10;
    data[data['id'] != 10]

10. ALTER TABLE table1 DROP COLUMN column_name;
    data.drop(column = 'column_name')
