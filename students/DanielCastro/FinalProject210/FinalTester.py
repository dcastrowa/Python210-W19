import DataProcessor as dp
import DataModel as dm

# Fill Products
pp = dp.ProductsProcessor(':memory:')

# Create a table for testing
crs = pp.db_con.cursor()
crs.execute("CREATE TABLE Products (ProductID int Primary Key, ProductName varchar(100));")
pp.db_con.commit()
pp.execute_sql_code(pp.build_ins_code(product_id=100, product_name='Mouse'))
pp.db_con.commit()
pp.execute_sql_code(pp.build_ins_code(product_id=200, product_name='Keyboard'))
pp.db_con.commit()

# print(pp.build_sel_code())
plst = []
for row in crs.execute(pp.build_sel_code()):
    # print(row)
    plst.append(dm.Product(row[0], row[1]))
print(plst)
pp.db_con.commit()
pp.db_con.close()

# Fill Inventory Counts
icp = dp.InventoryCountsProcessor(':memory:')

# Create table for testing
crs = icp.db_con.cursor()
crs.execute("CREATE TABLE InventoryCounts (InventoryCountID int, ProductID int, Count int);")
icp.db_con.commit()
icp.execute_sql_code(icp.build_ins_code(inv_count_id=11011, product_id=2019024, count=25))
icp.db_con.commit()
icp.execute_sql_code(icp.build_ins_code(inv_count_id=11012, product_id=2019025, count=25))
icp.db_con.commit()

print(icp.build_sel_code())
iclst = []
for row in crs.execute(icp.build_sel_code()):
    print(row)
    # adjust row indices to match input for Inventory object
    iclst.append(dm.InventoryCount(row[0], row[1]))
print(iclst)
icp.db_con.commit()
icp.db_con.close()
