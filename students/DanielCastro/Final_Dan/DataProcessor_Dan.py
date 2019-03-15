import sqlite3
from sqlite3 import Error as sqlErr
import re as rex

debugIP = True


class DBProcessor(object):

    def __init__(self, db_name: str = ":memory:"):  # Handy for testing!
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
                if rex.search(' or ', sql_str.split('WHERE')[1], rex.IGNORECASE) is not None:  # injected OR?
                    raise sqlErr("OR Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_str_type(sql_str):
        try:
            if sql_str is not str:
                raise sqlErr('Must be a string type')
        except Exception as e:
            raise e

    @staticmethod
    def check_for_int_type(sql_str):
        try:
            if sql_str is not int:
                raise sqlErr('Must be an integer')
        except Exception as e:
            raise e

    @staticmethod
    def check_for_date(date_str):
        """Checks for an valid date string"""
        try:
            if rex.match(r"\d\d\d\d-\d\d-\d\d", str(date_str)) is None:
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
                self.check_for_extra_semicolon(sql_code)
                self.check_for_or(sql_code)
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
        sql = str.format("INSERT Not Implemented Yet")
        return sql

    def build_upd_code(self):
        # Validate Input
        sql = str.format("UPDATE Not Implemented Yet")
        return sql

    def build_del_code(self):
        # Validate Input
        # Validate Input
        sql = str.format("DELETE Not Implemented Yet")
        return sql

    def build_sel_code(self):
        # Validate Input
        sql = str.format("SELECT Not Implemented Yet")
        return sql


class ProductsProcessor(DBProcessor):

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


class InventoryCountsProcessor(DBProcessor):

    def build_ins_code(self, inventory_id: int, product_id: int, count: int):
        sql = str.format("INSERT INTO InventoryCounts (InventoryID, ProductID, Count) "
                         "VALUES ({id},{pid},{count});", id=inventory_id, pid=product_id, count=count)
        return sql

    def build_upd_code(self, product_id: int, count: int):
        sql = str.format("UPDATE InventoryCounts SET Count = {count} "
                         "WHERE ProductID = {pid};", pid=product_id, count=count)
        return sql

    def build_del_code(self, product_id: int):
        sql = str.format("DELETE FROM InventoryCounts "
                         "WHERE ProductID = {id};", id=product_id)
        return sql

    def build_sel_code(self, product_id: int = None):
        if product_id is not None:
            w = ' WHERE ProductID = ' + str(product_id)
        else:
            w = ''
        sql = str.format("SELECT InventoryID, ProductID, Count "
                         "FROM InventoryCounts{WHERE};", WHERE=w)
        return sql


class InventoryProcessor(DBProcessor):

    def build_ins_code(self, inventory_id: int, inventory_date: str):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("INSERT INTO Inventories (InventoryID, InventoryDate) "
                         "VALUES ({id},'{date}');", id=inventory_id, date=inventory_date)
        return sql

    def build_upd_code(self, inventory_id: int, inventory_date: str):
        DBProcessor.check_for_date()
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


# if __name__ == '__main__':

    # Test DataProcessor methods
    # try:
    #     DBProcessor.check_for_or("SELECT * FROM T1 WHERE ID = 1 or 1 = 1")
    # except Exception as e:
    #     print(e)
    # try:
    #     DBProcessor.check_for_extra_semicolon("SELECT * ;Delete From T1; FROM T1;")
    # except Exception as e:
    #     print(e)
    # try:
    #     DBProcessor.check_for_date('01/01/2000')
    # except Exception as e:
    #     print(e)
    #
    # dbp = DBProcessor(':memory:')
    # print(dbp.build_ins_code())
    # print(dbp.build_upd_code())
    # print(dbp.build_del_code())
    # print(dbp.build_sel_code())
    # print(dbp.build_sel_code())
    # dbp.db_con.close()

    # if debugIP:
                          # ----- Debug InventoryProcessor -----
        # ip = InventoryProcessor(':memory:')
        # print(ip.build_ins_code(inventory_id=1, inventory_date='2000-01-01'))
        # print(ip.build_upd_code(inventory_id=1, inventory_date='2000-02-02'))
        # print(ip.build_del_code(inventory_id=1))
        # print(ip.build_sel_code())
        #
        # # Create a table for testing
        # crs = ip.db_con.cursor()
        # crs.execute("CREATE TABLE Inventories (InventoryID int, InventoryDate date);")
        # ip.db_con.commit()
        # for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
        #     print(row)
        # ip.db_con.commit()
        #
        # # Test SQL Transactions
        # ip.execute_sql_code(ip.build_ins_code(inventory_id=1, inventory_date='2000-01-01')).close()
        # for row in ip.execute_sql_code(ip.build_sel_code()):
        #     print(row)
        #
        # ip.execute_sql_code(ip.build_upd_code(inventory_id=1, inventory_date='2000-02-02')).close()
        # for row in ip.execute_sql_code(ip.build_sel_code(inventory_id=1)):
        #     print(row)
        #
        # ip.execute_sql_code(ip.build_del_code(inventory_id=1)).close()
        # for row in ip.execute_sql_code(ip.build_sel_code()):
        #     print(row)
        #
        #                 #  ----- Debug ProductsProcessor -----
        # pp = ProductsProcessor('/Users/danielcastro/Documents/sqlite-tools-osx-x86-3270200/databases/pp_test.db')
        # print(pp.build_ins_code(product_id=10, product_date='2019-02-14'))
        # print(pp.build_upd_code(product_id=10, product_date='2019-04-11'))
        # print(pp.build_del_code(product_id=10))
        # print(pp.build_sel_code())
        #
        # # Create a table for testing
        # crs = pp.db_con.cursor()
        # crs.execute("CREATE TABLE Products (ProductID int, ProductDate date);")
        # pp.db_con.commit()
        # for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
        #     print(row)
        # pp.db_con.commit()
        #
        # # Test SQL Transactions
        # pp.execute_sql_code(pp.build_ins_code(product_id=10, product_date='2019-02-14')).close()
        # for row in pp.execute_sql_code(pp.build_sel_code()):
        #     print(row)
        #
        # pp.execute_sql_code(pp.build_upd_code(product_id=10, product_date='2019-04-11')).close()
        # for row in pp.execute_sql_code(pp.build_sel_code(product_id=1)):
        #     print(row)
        #
        # pp.execute_sql_code(pp.build_del_code(product_id=10)).close()
        # for row in pp.execute_sql_code(pp.build_sel_code()):
        #     print(row)

                        #  ----- Debug InventoryCountsProcessor -----
        # icp = InventoryCountsProcessor(':memory:')
        # print(icp.build_ins_code(inv_count_id=11101011, product_id=1, count=25))
        # print(icp.build_upd_code(inv_count_id=11101011, count=420))
        # print(icp.build_del_code(inv_count_id=11101011))
        # print(icp.build_sel_code())
        #
        # # Create a table for testing
        # crs = icp.db_con.cursor()
        # crs.execute("CREATE TABLE InventoryCounts (InventoryCountID int, ProductId int, Count int);")
        # icp.db_con.commit()
        # for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
        #     print(row)
        # icp.db_con.commit()
        #
        # # Test SQL Transactions
        # icp.execute_sql_code(icp.build_ins_code(inv_count_id=11101011, product_id=1, count=25)).close()
        # for row in icp.execute_sql_code(icp.build_sel_code()):
        #     print(row)
        #
        # icp.execute_sql_code(icp.build_upd_code(inv_count_id=11101011, count=420)).close()
        # for row in icp.execute_sql_code(icp.build_sel_code(inv_count_id=11101011)):
        #     print(row)
        #
        # icp.execute_sql_code(icp.build_del_code(inv_count_id=11101011)).close()
        # for row in icp.execute_sql_code(icp.build_sel_code()):
        #     print(row)
