import tkinter as tk
# from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter.messagebox import *
import csv

from pandas import Index
import pandas
import pandas as pd
import json

import ctypes, threading

from utils import get_encoding_type, get_all_headers, unwrap_nester_hierarchy, check_nested_hierarchy, unwrap_nester_hierarchy_in_row
from updater import update

# from utils import get_encoding_type, get_ddl_type, get_engine_type
# from updater import update


class JsonParserApp:
    def __init__(self, master):
        self.filetypes = [("Json files", "*.json"), ]

        self.master = master
        self.master.title("Json Parser")

        self.label = tk.Label(master, text="Выбор Json файла")
        self.label.pack(padx=(25, 25), pady=(10, 10))

        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack(padx=(10, 10), pady=(10, 10))

        self.generate_button = tk.Button(master, text="Generate CSV file from JSON", command=self.generate_json)
        self.generate_button.pack(padx=(35, 35), pady=(10, 25))

    def select_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=self.filetypes)
        self.label.config(text="Выбранный файл: " + self.filepath)

    def generate_json(self):
        try:
            if self.filepath:
                if self.filepath.endswith('.json'):
                    # try:
                    #     #df = pandas.read_json(self.filepath, lines=True)
                    #     data = []
                    #     with open(self.filepath) as f:
                    #         for line in f:
                    #             data.append(json.loads(line))

                        # for i in range(len(df.columns)):
                        #     print(df[f"{df.columns[i]}"])
                    # except UnicodeDecodeError as unicode_error:
                    encoding = get_encoding_type(self.filepath)
                    data = []
                    with open(self.filepath, encoding=encoding) as f:
                        for line in f:
                            data.append(json.loads(line))

                    # for dict_row in data:
                    #     if check_nested_hierarchy(dict_row) == True:
                    #         unwrap_nester_hierarchy_in_row(data)

                    unwrap_nester_hierarchy(data)

                    headers = get_all_headers(data)
                    print(headers)
                    # for i in range(len(data)):
                    #     data[i] = str(data[i])

                    # with open("csv_file.csv", 'w', newline='', encoding=encoding) as csvfile:
                    #     writer = csv.DictWriter(csvfile, fieldnames=headers)
                    #     writer.writeheader()
                    #     for row in data:
                    #         writer.writerow(row)
                        #writer.writerows(data)

                    with open("csv_file.csv", 'w', newline='', encoding=encoding) as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(headers)
                        for row in data:
                            writer.writerow([[row.get(key, None) for key in headers]])        #rowdict.get(key, self.restval) for key in self.fieldnames          #writer.writerow([list(row.values())]) #[value for value in row.values()]

                    #df = pandas.read_json(self.filepath, lines=True, encoding=get_encoding_type(self.filepath))
                else:
                    messagebox.showerror("Error", "Unsupported file format")
                    return

            else:
                messagebox.showerror("Error", "No file selected")
        except Exception as e:
            messagebox.showerror("Error", str(e) + " " + str(e.__class__.__name__))
            print("Error", str(e) + " " + str(e.__class__.__name__))



def main():
    root = tk.Tk()
    app = JsonParserApp(root)
    root.mainloop()




if __name__ == "__main__":
    update()
    main()