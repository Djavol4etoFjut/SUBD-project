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
