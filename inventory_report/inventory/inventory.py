import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    @classmethod
    def import_data(self, file_path, string_type):
        inventory_list = []
        if "csv" in file_path:
            with open(file_path, encoding="utf-8") as f:
                file_reader = csv.DictReader(f, delimiter=",", quotechar='"')

                for item in file_reader:
                    inventory_list.append(item)

        if "json" in file_path:
            with open(file_path) as file:
                content = file.read()
                inventory_list = json.loads(content)

        if string_type == "simples":
            return SimpleReport.generate(inventory_list)
        else:
            return CompleteReport.generate(inventory_list)
