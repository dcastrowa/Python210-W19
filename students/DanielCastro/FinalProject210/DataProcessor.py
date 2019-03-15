# Desc: Python 210 Final Simple Data Processor
# ChangeLog: (When,Who,What)
# 2/28/19,RRoot,Created Script

import sqlite3
from sqlite3 import Error as sqlErr
import re as rex


class DBProcessor(object):

    def __init__(self, db_name: str=":memory:"):
        self.__db_name = db_name
        self.__db_con = self.create_connection(self.db_name)

    @property
    def db_name(self):  # Get DB Name
        return self.__db_name

    @property
    def db_con(self):  # Get Live Connection
        return self.__db_con


    # SQL Validators

    @staticmethod
    def check_for_extra_semicolon(sql_str):
        """Checks for an extra semicolon"""
        # print(len("Select;Delete From T1; ID, Name FROM T1;".split(';')) > 2)
        try:
            if len(sql_str.split(';')) > 2:
                raise sqlErr("Extra Semi-Colon Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_or(sql_str):
        """Checks for an injected OR in tampered WHERE Clause"""
        # print(rex.search("WHERE", "SELECT * FROM T1 WHERE", rex.IGNORECASE))
        # print(rex.search("or","FROM T1 WHERE ID = 1 or 1 = 1".split('WHERE')[1], rex.IGNORECASE))
        try:
            if rex.search("WHERE", sql_str, rex.IGNORECASE):  # If it has a Where clause
                if rex.search(' or ', sql_str.split('WHERE')[1], rex.IGNORECASE) is not None:  # check for injected OR
                    raise sqlErr("OR Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_date(date_str):
        try:
            if rex.match("\d\d\d\d-\d\d-\d\d", str(date_str)) is None:
                raise sqlErr("Not a Date!")
        except Exception as e:
            raise e

    def create_connection(self, db_file: str):
        """ Create or connect to a SQLite database """
        try:
            con = sqlite3.connect(db_file)
        except sqlErr as se:
            raise Exception('SQL Error in create_connection(): ' + se.__str__())
        except Exception as e:
            raise Exception('General Error in create_connection(): ' + e.__str__())
        return con

    def execute_sql_code(self, sql_code: str = ''):
        """ Execute SQL code on a open connection """
        db_con = self.db_con
        try:
            if db_con is not None and sql_code != '':
                # Validate
                self.check_for_extra_semicolon(sql_code);
                self.check_for_or(sql_code);
                # Connect and Run
                with db_con:
                    csr = db_con.cursor()
                    csr.execute(sql_code)
            else:
                raise Exception('SQL Code or Connection is missing!')
        except sqlErr as se:
            raise Exception('SQL Error in execute_sql_code(): ' + se.__str__())
        except Exception as e:
            raise Exception('General Error in execute_sql_code(): ' + e.__str__())
        return csr

    def build_ins_code(self):
        # Validate Input
        # Build Code
        sql = str.format("INSERT Not Implemented Yet")
        return sql

    def build_upd_code(self):
        # Validate Input
        # Build Code
        sql = str.format("UPDATE Not Implemented Yet")
        return sql

    def build_del_code(self):
        # Validate Input
        # Build Code
        sql = str.format("DELETE Not Implemented Yet")
        return sql

    def build_sel_code(self):
        # Validate Input
        # Build Code
        sql = str.format("SELECT Not Implemented Yet")
        return sql

class InventoryProcessor(DBProcessor):

    def build_ins_code(self, inventory_id: int, inventory_date: str):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("INSERT INTO Inventories (InventoryID, InventoryDate) "
                         "VALUES ({id},'{date}');", id=inventory_id, date=inventory_date)
        return sql

    def build_upd_code(self, inventory_id: int, inventory_date: str ):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("UPDATE Inventories SET InventoryDate = '{date}' "
                         "WHERE InventoryID = {id};", id=inventory_id, date=inventory_date)
        return sql

    def build_del_code(self, inventory_id: int):
        sql = str.format("DELETE FROM Inventories "
                         "WHERE InventoryID = {id};", id=inventory_id)
        return sql

    def build_sel_code(self, inventory_id: int = None):
        if inventory_id is not None:
            w = ' WHERE InventoryID = ' + str(inventory_id)
        else:
            w = ''
        sql = str.format("SELECT InventoryID, InventoryDate "
                         "FROM Inventories{WHERE};", WHERE=w)
        return sql

class ProductProcessor(DBProcessor):

    def build_ins_code(self, product_id: int, product_name: str):
        sql = str.format("INSERT INTO Products (ProductID, ProductName) "
                         "VALUES ({id},'{name}');", id=product_id, name=product_name)
        return sql

    def build_upd_code(self, product_id: int, product_name: str):
        sql = str.format("UPDATE Products SET ProductName = '{name}' "
                         "WHERE ProductID = {id};", id=product_id, name=product_name)
        return sql

    def build_del_code(self, product_id: int):
        sql = str.format("DELETE FROM Products "
                         "WHERE ProductID = {id};", id=product_id)
        return sql

    def build_sel_code(self, product_id: int = None):
        if product_id is not None:
            w = ' WHERE ProductID = ' + str(product_id)
        else:
            w = ''
        sql = str.format("SELECT ProductID, ProductName "
                         "FROM Products{WHERE};", WHERE=w)
        return sql


class InventoryCountProcessor(DBProcessor):

    def build_ins_code(self, inventory_id: int, product_id: int, count: int):
        sql = str.format("INSERT INTO InventoryCounts (InventoryID, ProductID, Count) "
                         "VALUES ({iid}, {pid},'{cnt}');", iid=inventory_id, pid=product_id, cnt=count)
        return sql

    def build_upd_code(self, inventory_id: int, product_id: int, count: int):
        sql = str.format("UPDATE InventoryCounts SET Count = {cnt} "
                         "WHERE InventoryID = {iid} "
                         "AND ProductID = {pid};", iid=inventory_id, pid=product_id, cnt=count)
        return sql

    def build_del_code(self, inventory_id: int, product_id: int):
        sql = str.format("DELETE FROM InventoryCounts "
                         "WHERE InventoryID = {iid} AND ProductID = {pid};", iid=inventory_id, pid=product_id)
        return sql

    def build_sel_code(self, inventory_id: int = None, product_id: int = None):
        if inventory_id is not None and product_id is None:
            w = ' WHERE InventoryID = ' + str(inventory_id)
        elif inventory_id is None and product_id is not None:
            w = ' WHERE ProductID = ' + str(product_id)
        elif inventory_id is not None and product_id is not None:
            w = ' WHERE InventoryID = ' + str(inventory_id) + ' AND ProductID = ' + str(product_id)
        else:
            w = ''
        sql = str.format("SELECT InventoryId, ProductID, Count "
                         "FROM InventoryCounts{WHERE};", WHERE=w)
        return sql
