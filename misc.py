import sqlite3

def add_to_countries_table(conn, values):
    sql = """INSERT INTO countries(name, climate)
                VALUES(?,?)"""
    with conn:
        c = conn.cursor()
        c.execute(sql,values)

def add_to_forest_type_table(conn, values):
    sql = """INSERT INTO forest_types(type,natural,conserved)
            VALUES(?,?,?)"""
    with conn:
        c = conn.cursor()
        c.execute(sql,values)

def add_to_forest_table(conn, values):
    sql = """INSERT INTO forests(len,lat,country_name,forest_type_id)
            VALUES(?,?,?,?)"""
    with conn:
        c = conn.cursor()
        c.execute(sql,values)

def forest_table_to_str(conn):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM forests")
        rows = c.fetchall()
        string = ''
        i=0
        for row in rows:
            string = string + ''.join(str(rows[i]))
            string = string + '\n'
            i=i+1
        return string

def forest_type_table_to_str(conn):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM forest_types")
        rows = c.fetchall()
        string = ''
        i=0
        for row in rows:
            string = string + ''.join(str(rows[i]))
            string = string + '\n'
            i=i+1
        return string

def countries_table_to_str(conn):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM countries")
        rows = c.fetchall()
        string = ''
        i=0
        for row in rows:
            string = string + ''.join(str(rows[i]))
            string = string + '\n'
            i=i+1
        return string

def whole_db_to_string(conn):
    string = forest_table_to_str(conn)
    string = string + forest_type_table_to_str(conn)
    string = string + countries_table_to_str(conn)
    return string

