import pyodbc
import UntilConfig as uConfig

#初始化删除表里面所有数据
def del_table(sheet_name):
    db_file = uConfig.mdb_path
    conn_str = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=" + db_file
    conn = pyodbc.connect(conn_str)
    try:
        # 2. 创建游标
        cursor = conn.cursor()

        # 3. 执行 DELETE 语句
        delete_query = f"DELETE FROM {sheet_name}"
        cursor.execute(delete_query)

        # 4. 提交事务（如果需要）
        conn.commit()

        print("数据删除成功")
    except Exception as e:
        print("发生错误:", e)
    finally:
        # 5. 关闭游标和连接
        cursor.close()
        conn.close()


def insert_data(sheet_name, fields, values):
    # 连接到Access数据库
    db_file = uConfig.mdb_path
    conn_str = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=" + db_file
    conn = pyodbc.connect(conn_str)

    try:
        # 构建INSERT语句
        insert_query = f"INSERT INTO {sheet_name} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in fields])})"
        # 执行插入
        cursor = conn.cursor()
        cursor.execute(insert_query, values)
        conn.commit()
        print(fields)
        print(values)
        print("数据插入成功！")
        conn.close()

        return "数据插入成功"
    except Exception as e:
        print(f"插入数据时出现错误：{e}")
        conn.rollback()
        conn.close()

        return f"插入数据时出现错误：{e}"



