import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    def import_csv(file_path):
        inventory_list = []
        with open(file_path, encoding="utf-8") as f:
            file_reader = csv.DictReader(f, delimiter=",", quotechar='"')

        for item in file_reader:
            inventory_list.append(item)

        return inventory_list

    def import_json(file_path):
        inventory_list = []
        with open(file_path) as file:
            read_file = file.read()
            inventory_list = json.loads(read_file)

        return inventory_list

    def import_xml(file_path):
        inventory_list = []
        with open(file_path) as file:
            read_file = xmltodict.parse(file.read())
            inventory_list = read_file["dataset"]["record"]

        return inventory_list

    @classmethod
    def import_data(self, file_path, string_type):
        if "csv" in file_path:
            inventory_list = self.import_csv(file_path)

        if "json" in file_path:
            inventory_list = self.import_json(file_path)

        if "xml" in file_path:
            inventory_list = self.import_xml(file_path)

        if string_type == "simples":
            return SimpleReport.generate(inventory_list)
        else:
            return CompleteReport.generate(inventory_list)
