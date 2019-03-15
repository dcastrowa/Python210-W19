import tkinter as tk
from tkinter import ttk
import DataModel as dm
import DataProcessor as dp

database = '/Users/danielcastro/Documents/sqlite-tools-osx-x86-3270200/databases/''Python210FinalDB.db'


class IOProcessor:

    # Product
    @staticmethod
    def sel_product(text_widget):
        products = []
        pp = dp.ProductProcessor(database)
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            products.append(dm.Product(row[0], row[1]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if products is None:
            text_widget.insert("No data available")
        else:
            text_widget.insert(tk.END, "ProductID,ProductName\n")
            for row in products:
                print(row, type(row))
                text_widget.insert(tk.END, str(row) + "\n")

        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_product(product_id, product_name, update_controls=[None]):
        pp = dp.ProductProcessor(database)
        sql = pp.build_ins_code(product_id=product_id, product_name=product_name)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    @staticmethod
    def upd_product(product_id, product_name, update_controls=[None]):
        pp = dp.ProductProcessor(database)
        sql = pp.build_upd_code(product_id=product_id, product_name=product_name)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    @staticmethod
    def del_product(product_id, update_controls=[None]):
        pp = dp.ProductProcessor(database)
        sql = pp.build_del_code(product_id=product_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    # Inventory Count
    @staticmethod
    def sel_inventory_count(text_widget):
        inventory_count = []
        icp = dp.InventoryCountProcessor(database)
        sql = icp.build_sel_code()
        for row in icp.execute_sql_code(sql):
            inventory_count.append(dm.InventoryCount(row[0], row[1], row[2]))
        icp.db_con.commit()
        icp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if inventory_count is None:
            text_widget.insert("No data available")
        else:
            text_widget.insert(tk.END, "InventoryID,ProductID,Count\n")
            for row in inventory_count:
                print(row, type(row))
                text_widget.insert(tk.END, str(row) + "\n")

        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_inventory_count(inventory_id, product_id, count, update_controls=[None]):
        ip = dp.InventoryCountProcessor(database)
        sql = ip.build_ins_code(inventory_id=inventory_id, product_id=product_id, count=count)
        ip.execute_sql_code(sql)
        ip.db_con.commit()
        ip.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory_count(update_controls[0])

    @staticmethod
    def upd_inventory_count(inventory_id, product_id, count, update_controls=[None]):
        ip = dp.InventoryCountProcessor(database)
        sql = ip.build_upd_code(inventory_id=inventory_id, product_id=product_id, count=count)
        ip.execute_sql_code(sql)
        ip.db_con.commit()
        ip.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory_count(update_controls[0])

    @staticmethod
    def del_inventory_count(inventory_id, product_id, update_controls=[None]):
        ip = dp.InventoryCountProcessor(database)
        sql = ip.build_del_code(inventory_id=inventory_id, product_id=product_id)
        ip.execute_sql_code(sql)
        ip.db_con.commit()
        ip.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory_count(update_controls[0])

    # Inventory
    @staticmethod
    def sel_inventory(text_widget):
        inventory = []
        ip = dp.InventoryProcessor(database)
        sql = ip.build_sel_code()
        for row in ip.execute_sql_code(sql):
            inventory.append(dm.Inventory(row[0], row[1]))
        ip.db_con.commit()
        ip.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if inventory is None:
            text_widget.insert("No data available")
        else:
            text_widget.insert(tk.END, "InventoryID,InventoryDate\n")
            for row in inventory:
                print(row, type(row))
                text_widget.insert(tk.END, str(row) + "\n")

        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_inventory(inventory_id, inventory_date, update_controls=[None]):
        ip = dp.InventoryProcessor(database)
        sql = ip.build_ins_code(inventory_id=inventory_id, inventory_date=inventory_date)
        ip.execute_sql_code(sql)
        ip.db_con.commit()
        ip.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])

    @staticmethod
    def upd_inventory(inventory_id, inventory_date, update_controls=[None]):
        ip = dp.InventoryProcessor(database)
        sql = ip.build_upd_code(inventory_id=inventory_id, inventory_date=inventory_date)
        ip.execute_sql_code(sql)
        ip.db_con.commit()
        ip.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])

    @staticmethod
    def del_inventory(inventory_id, update_controls=[None]):
        ip = dp.InventoryProcessor(database)
        sql = ip.build_del_code(inventory_id=inventory_id)
        ip.execute_sql_code(sql)
        ip.db_con.commit()
        ip.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])


class MainWindow:
    """
    Desc: Creates the following UI objects
     -- window_root tk.TK
       -- notebook_frame ttk.Notebook
          -- tab_products tk.Frame
             -- lbl_product_info ttk.label
             -- btn_sel_product_info ttk.button
             -- mtx_product_info ttk.text
             -- lbl_product_id ttk.label
             -- txt_product_id ttk.entry
             -- lbl_product_name ttk.label
             -- txt_product_name ttk.entry
             -- btn_ins_product_info ttk.button
             -- btn_upd_product_info ttk.button
             -- btn_del_product_info ttk.button
          -- tab_inventories tk.Frame
          -- tab_inventory_counts tk.Frame
    """
    def __init__(self):
        self.window = tk.Tk()  # creates an root node
        self.window['padx'] = 10
        self.window['pady'] = 10
        self.notebook = ttk.Notebook(self.window)
        self.configure_notebook(self.notebook)  # create and configure tab container

    def configure_notebook(self, notebook_frame):
        notebook_frame.grid(row=4, column=2, sticky=tk.W, padx=20, pady=10)
        self.products_tab(notebook_frame)
        self.inventories_tab(notebook_frame)
        self.inventory_counts_tab(notebook_frame)
        return notebook_frame

    def products_tab(self, notebook_frame):
        tab_products = tk.Frame(notebook_frame)
        notebook_frame.add(tab_products, text="Products", compound=tk.TOP)

        btn_sel_product_info = ttk.Button(tab_products, text="Select Product Info", width=20)
        btn_sel_product_info.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        btn_sel_product_info["command"] = lambda: IOProcessor.sel_product(mtx_product_info)

        mtx_product_info = tk.Text(tab_products, width=55, height=10)
        mtx_product_info.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

        lbl_product_id = ttk.Label(tab_products, text="Product ID ", width=20, anchor=tk.E)
        lbl_product_id.grid(row=4, column=1, sticky=tk.E)
        txt_product_id = ttk.Entry(tab_products, width=50)
        txt_product_id.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        lbl_product_Name = ttk.Label(tab_products, text="Product Name ", width=20, anchor=tk.E)
        lbl_product_Name.grid(row=5, column=1, sticky=tk.E)
        txt_product_Name = ttk.Entry(tab_products, width=50)
        txt_product_Name.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        btn_ins_product_info = ttk.Button(tab_products, text="Insert Product Info", width=20)
        btn_ins_product_info.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
        btn_ins_product_info["command"] = lambda: IOProcessor.ins_product(txt_product_id.get(),
                                                                          txt_product_Name.get(),
                                                                          [mtx_product_info])

        btn_upd_product_info = ttk.Button(tab_products, text="Update Product Info", width=20)
        btn_upd_product_info.grid(row=6, column=2, sticky=tk.EW, padx=5, pady=5)
        btn_upd_product_info["command"] = lambda: IOProcessor.upd_product(txt_product_id.get(),
                                                                          txt_product_Name.get(),
                                                                          [mtx_product_info])

        btn_del_product_info = ttk.Button(tab_products, text="Delete Product Info", width=20)
        btn_del_product_info.grid(row=6, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_product_info["command"] = lambda: IOProcessor.del_product(txt_product_id.get(),
                                                                          [mtx_product_info])

    def inventories_tab(self, notebook_frame):
        tab_inventories = tk.Frame(notebook_frame)
        notebook_frame.add(tab_inventories, text="Inventories", compound=tk.TOP)

        btn_sel_inventory_info = ttk.Button(tab_inventories, text="Select Inventory Info", width=20)
        btn_sel_inventory_info.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        btn_sel_inventory_info["command"] = lambda: IOProcessor.sel_inventory(mtx_inventory_info)

        mtx_inventory_info = tk.Text(tab_inventories, width=55, height=10)
        mtx_inventory_info.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

        lbl_inventory_id = ttk.Label(tab_inventories, text="Inventory ID ", width=20, anchor=tk.E)
        lbl_inventory_id.grid(row=4, column=1, sticky=tk.E)
        txt_inventory_id = ttk.Entry(tab_inventories, width=50)
        txt_inventory_id.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        lbl_inventory_date = ttk.Label(tab_inventories, text="Inventory Date ", width=20, anchor=tk.E)
        lbl_inventory_date.grid(row=5, column=1, sticky=tk.E)
        txt_inventory_date = ttk.Entry(tab_inventories, width=50)
        txt_inventory_date.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        btn_ins_inventory_info = ttk.Button(tab_inventories, text="Insert Inventory Info", width=20)
        btn_ins_inventory_info.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
        btn_ins_inventory_info["command"] = lambda: IOProcessor.ins_inventory(txt_inventory_id.get(),
                                                                              txt_inventory_date.get(),
                                                                              [mtx_inventory_info])

        btn_upd_inventory_info = ttk.Button(tab_inventories, text="Update Inventory Info", width=20)
        btn_upd_inventory_info.grid(row=6, column=2, sticky=tk.EW, padx=5, pady=5)
        btn_upd_inventory_info["command"] = lambda: IOProcessor.upd_inventory(txt_inventory_id.get(),
                                                                              txt_inventory_date.get(),
                                                                              [mtx_inventory_info])

        btn_del_inventory_info = ttk.Button(tab_inventories, text="Delete Inventory Info", width=20)
        btn_del_inventory_info.grid(row=6, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_inventory_info["command"] = lambda: IOProcessor.del_inventory(txt_inventory_id.get(),
                                                                          [mtx_inventory_info])

    def inventory_counts_tab(self, notebook_frame):
        tab_inventory_counts = tk.Frame(notebook_frame)
        notebook_frame.add(tab_inventory_counts, text="Inventory Counts", compound=tk.TOP)

        btn_sel_inv_count_info = ttk.Button(tab_inventory_counts, text="Select Inventory Count Info", width=20)
        btn_sel_inv_count_info.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        btn_sel_inv_count_info["command"] = lambda: IOProcessor.sel_inventory_count(mtx_inv_count_info)

        mtx_inv_count_info = tk.Text(tab_inventory_counts, width=55, height=10)
        mtx_inv_count_info.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

        lbl_inv_id = ttk.Label(tab_inventory_counts, text="Inventory ID ", width=20, anchor=tk.E)
        lbl_inv_id.grid(row=4, column=1, sticky=tk.E)
        txt_inventory_id = ttk.Entry(tab_inventory_counts, width=50)
        txt_inventory_id.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        lbl_product_id = ttk.Label(tab_inventory_counts, text="Product ID ", width=20, anchor=tk.E)
        lbl_product_id.grid(row=5, column=1, sticky=tk.E)
        txt_product_id = ttk.Entry(tab_inventory_counts, width=50)
        txt_product_id.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        lbl_count = ttk.Label(tab_inventory_counts, text="Count ", width=20, anchor=tk.E)
        lbl_count.grid(row=6, column=1, sticky=tk.E)
        txt_count = ttk.Entry(tab_inventory_counts, width=50)
        txt_count.grid(row=6, column=2, padx=5, pady=5, columnspan=2)

        btn_ins_inv_count_info = ttk.Button(tab_inventory_counts, text="Insert Inventory Count Info", width=20)
        btn_ins_inv_count_info.grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)
        btn_ins_inv_count_info["command"] = lambda: IOProcessor.ins_inventory_count(txt_inventory_id.get(),
                                                                                    txt_product_id.get(),
                                                                                    txt_count.get(),
                                                                                    [mtx_inv_count_info])

        btn_upd_inv_count_info = ttk.Button(tab_inventory_counts, text="Update Inventory Info", width=20)
        btn_upd_inv_count_info.grid(row=7, column=2, sticky=tk.EW, padx=5, pady=5)
        btn_upd_inv_count_info["command"] = lambda: IOProcessor.upd_inventory_count(txt_inventory_id.get(),
                                                                                    txt_product_id.get(),
                                                                                    txt_count.get(),
                                                                                    [mtx_inv_count_info])

        btn_del_inv_count_info = ttk.Button(tab_inventory_counts, text="Delete Inventory Info", width=20)
        btn_del_inv_count_info.grid(row=7, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_inv_count_info["command"] = lambda: IOProcessor.del_inventory_count(txt_inventory_id.get(),
                                                                                    txt_product_id.get(),
                                                                                    [mtx_inv_count_info])


if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()



