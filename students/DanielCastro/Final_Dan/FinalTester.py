import DataProcessor as dp
import DataModel as dm

# Fill Products
pp = dp.ProductsProcessor(':memory:')

# Create a table for testing
crs = pp.db_con.cursor()
crs.execute("CREATE TABLE Products (ProductID int Primary Key, ProductName varchar(100));")
pp.db_con.commit()
pp.execute_sql_code(pp.build_ins_code(product_id=1, product_name='Mouse'))
pp.db_con.commit()
pp.execute_sql_code(pp.build_ins_code(product_id=2, product_name='Keyboard'))
pp.db_con.commit()

# print(pp.build_sel_code())
plst = []
for row in crs.execute(pp.build_sel_code()):
    # print(row)
    plst.append(dm.Product(row[0], row[1]))
# print(plst)
pp.db_con.commit()
pp.db_con.close()

# Fill Inventory Counts
icp = dp.InventoryCountsProcessor(':memory:')

# Create table for testing
crs = icp.db_con.cursor()
crs.execute("CREATE TABLE InventoryCounts (InventoryID int, ProductID int, Count int);")
icp.db_con.commit()
icp.execute_sql_code(icp.build_ins_code(inventory_id=11011, product_id=1, count=25))
icp.db_con.commit()
icp.execute_sql_code(icp.build_ins_code(inventory_id=11011, product_id=2, count=15))
icp.db_con.commit()

# print(icp.build_sel_code())
iclst = []

for product in plst:
    for tbl_row in crs.execute(icp.build_sel_code()):
        iclst.append(dm.InventoryCount(tbl_row[0], product, tbl_row[2]))
print(iclst)

# for f, b in zip(plst, crs.execute(icp.build_sel_code())):
#     # print(f, b)
#     iclst.append(dm.InventoryCount(plst[0], b[2]))
# print(iclst)
# icp.db_con.commit()
# icp.db_con.close()


# ip = dp.InventoryProcessor(':memory:')
#
# # Create table for testing
# crs = ip.db_con.cursor()
# crs.execute("CREATE TABLE Inventories (InventoryID int, InventoryDate date);")
# ip.db_con.commit()
# ip.execute_sql_code(ip.build_ins_code(inventory_id=11011, inventory_date='2019-04-11'))
# ip.db_con.commit()
# ip.execute_sql_code(ip.build_ins_code(inventory_id=11012, inventory_date='2019-04-20'))
# ip.db_con.commit()


# figure out how to
# print(ip.build_sel_code())
# ilst = []
# for f, b in zip(iclst, crs.execute(ip.build_sel_code())):
#     print(iclst[0], b[0])
# #     ilst.append(dm.Inventory(b[0], b[1], iclst[2]))
# # print(iclst)
# # ip.db_con.commit()
# # ip.db_con.close()
