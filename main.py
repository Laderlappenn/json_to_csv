import tkinter as tk
from tkinter import filedialog, messagebox
import csv

import json

from utils import get_encoding_type, get_all_headers, unwrap_nester_hierarchy, check_nested_hierarchy, unwrap_nester_hierarchy_in_row
from updater import update



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
                    encoding = get_encoding_type(self.filepath)
                    data = []
                    with open(self.filepath, encoding=encoding) as f:
                        for line in f:
                            data.append(json.loads(line))

                    unwrap_nester_hierarchy(data)
                    headers = get_all_headers(data)
                    print(headers)

                    #this is sad
                    headers.remove('digiSign')
                    headers.remove('executorDigiSign')

                    with open("csv_file.csv", 'w', newline='', encoding=encoding) as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(headers)
                        for row in data:
                            complete_row = []
                            for key in headers:
                                complete_row.append(row.get(key, None))

                            writer.writerow(complete_row)
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