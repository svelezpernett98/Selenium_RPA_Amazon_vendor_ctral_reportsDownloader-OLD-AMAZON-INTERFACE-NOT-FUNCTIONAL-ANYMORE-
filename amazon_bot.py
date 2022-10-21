from pickle import TRUE
from typing import final
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, os
import tkinter as tk
from tkinter import ttk
from selenium.webdriver.common.action_chains import ActionChains

dir = os.getcwd()
PATH = str(dir)+"/chromedriver.exe"
picture_options = Options()
picture_options.add_argument("--start-maximized")

init = webdriver.Chrome(PATH, chrome_options=picture_options)  
init.get("https://vendorcentral.amazon.com")
user = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.ID, 'ap_email')))
user.send_keys("test@email.co")
pwd = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.ID, 'ap_password')))
pwd.send_keys("PASSWORD")

enter_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.ID, 'signInSubmit'))).click()

class App(ttk.Frame):
    def __init__(self, parent):
        value_input="defaullt"
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):   
        def show_msg():
            print("melo")
            value_OTC = self.entry.get()
            print(value_OTC)
            OTC_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input')))
            OTC_input.send_keys(value_OTC)
            time.sleep(5)
            submit_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/span/span/input'))).click()
            
            print("submit click check") 
             
            reports_drop_down_list = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div/div[2]/div[5]/span')))
            
            hover = ActionChains(init).move_to_element(reports_drop_down_list)
            hover.perform()
            analytics_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div/div[2]/div[5]/div/a[2]'))).click()
            
            print("hoover check") 
            
            # sales_diagnostics_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/ul/li[1]/div/div/div/span[1]/a'))).click()

            distributor_view_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[1]/span[2]/div/awsui-button-dropdown/div/awsui-button/button'))).click()

            sourcing_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[1]/span[2]/div/awsui-button-dropdown/div/div/ul/li[2]'))).click()
            
            sales_view_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[1]/span[3]/div/awsui-button-dropdown/div/awsui-button/button'))).click()
            
            #tambien hacer con la otra opcion
            shipped_revenue_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[1]/span[3]/div/awsui-button-dropdown/div/div/ul/li[1]'))).click()
            
            reporting_range_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[1]/div/awsui-button-dropdown/div/awsui-button/button'))).click()

            monthly_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[1]/div/awsui-button-dropdown/div/div/ul/li[3]'))).click()
            
            
            
            #month_label = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]'))).text
            #print(month_label)
            #initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[6]'))).click()

            #final_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[6]/div[1]'))).click()
            
            time.sleep(1)
            
            def date_picker_loop(sales_view):
                for i in range(21):
                    date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                    file_name = ""
                    print(i)
                    if i == 0:
                        month_label = "January 2021"
                        month_label_value = ""
                        while month_label != month_label_value:
                            left_Arrow_date = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/a[1]'))).click()
                            time.sleep(0.3)
                            month_label_value = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]'))).text
                            print(month_label_value)
                        print("enero 01")
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[6]'))).click()
                        
                        month_label = "January 2021"
                        month_label_value = "" 
                        while month_label != month_label_value:
                            left_Arrow_date = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/a[1]'))).click()
                            time.sleep(0.3)
                            month_label_value = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]'))).text
                            print(month_label_value)
                        print("enero 31")
                        final_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[6]/div[1]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Enero2021_" + sales_view)
                    if i == 1:
                        print("febrero")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[2]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Febrero2021_" + sales_view)
                    if i == 2:
                        print("marzo")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[2]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Marzo2021_" + sales_view)
                    if i == 3:
                        print("abril")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[5]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Abril2021_" + sales_view)
                    if i == 4:
                        print("mayo")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[7]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Mayo2021_" + sales_view)
                    if i == 5:
                        print("junio")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[3]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Junio2021_" + sales_view)
                    if i == 6:
                        print("julio")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[5]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Julio2021_" + sales_view)
                    if i == 7:
                        print("agosto")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[1]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Agosto2021_" + sales_view)
                    if i == 8:
                        print("septiembre")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[4]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Septiembre2021_" + sales_view)
                    if i == 9:
                        print("octubre")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[6]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Octubre2021_" + sales_view)
                    if i == 10:
                        print("noviembre")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[2]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Noviembre2021_" + sales_view)
                    if i == 11:
                        print("diciembre")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[4]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Diciembre2021_" + sales_view)
                        
                    if i == 12:
                        print("enero22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[7]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Enero2022_" + sales_view)
                        
                    if i == 13:
                        print("febrero22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[3]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Febrero2022_" + sales_view)
                        
                    if i == 14:
                        print("marzo22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[3]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Marzo2022_" + sales_view)
                        
                    if i == 15:
                        print("abril22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[6]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Abril2022_" + sales_view)
                        
                    if i == 16:
                        print("mayo22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[1]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Mayo2022_" + sales_view)
                        
                    if i == 17:
                        print("junio22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[4]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Junio2022_" + sales_view)
                        
                    if i == 18:
                        print("julio22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[6]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Julio2022_" + sales_view)
                        
                    if i == 19:
                        print("agosto22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[2]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Agosto2022_" + sales_view)
                        
                    if i == 20:
                        print("septiembre22")
                        date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[3]/span[2]/div/span/span'))).click()
                        initial_date_input = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[3]/div[2]/div[1]/div[5]'))).click()
                        file_name = ("Sales_Diagnostics_Us_Septiembre2022_" + sales_view)
                        
                    #/html/body/div[3]/div/div[3]/div[2]/div[1]/div[7]
                    apply_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[4]/span/div/awsui-button[2]/button'))).click()
                    time.sleep(10)
                    download_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[1]/div[2]/div/div[1]/awsui-button-dropdown/div/awsui-button/button'))).click()
                    as_excel_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[1]/div[2]/div/div[1]/awsui-button-dropdown/div/div/ul/li[1]/ul/li[1]'))).click()
                    print("downloading...")
                    time.sleep(38)
                    init.switch_to.alert.accept()
                    print("alert accepted")
                    time.sleep(10)
                    
                    
                    # Absolute path of a file
                    old_name = "ROUTE/Sales Diagnostic_US.xlsx"
                    new_name = "ROUTE/"+str(file_name)+".xlsx"

                    # Renaming the file
                    os.rename(old_name, new_name)
                    
                #a nivel de este for i in range (21) poner el codigo de OStest.py, 
                # cambiar la ruta de descarga a alguna carpeta en documentos, y añadir 
                # un parametro a la hora de llamar la funcion date_picker_loop para el nombre del archivo multiple_sheets.xlsx
            
            shipped_rvnue = "shipped_revenue"
            date_picker_loop(shipped_rvnue)  
            
            sales_view_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[1]/span[3]/div/awsui-button-dropdown/div/awsui-button/button'))).click()    
            shipped_COGS_btn = WebDriverWait(init, 300).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[7]/div[2]/div/div[1]/span[3]/div/awsui-button-dropdown/div/div/ul/li[2]'))).click()
            print("changed to COGS")
            COGS = "COGS"
            date_picker_loop(COGS) 
                
        # # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "OTP")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        # # Button
        self.button = ttk.Button(self.widgets_frame, text= "Click Here", command=show_msg)
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        
            


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme  C:\Users\svelez\Desktop\Azure-ttk-theme\azure.tcl
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()



    
