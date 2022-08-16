from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():
    def get_products_quantity_by_company(self, stock):
        count_companies = list()
        final_string = ""

        for product in stock:
            count_companies.append(product["nome_da_empresa"])

        # https://www.delftstack.com/pt/howto/python/python-counter-most-common/
        most_common_company = Counter(count_companies).most_common()

        for product, quantity in most_common_company:
            final_string += f"- {product}: {quantity}\n"

        return final_string

    @classmethod
    def generate(self, stock):
        report = SimpleReport.generate(stock)
        products_list = self.get_products_quantity_by_company(self, stock)

        return (
            f"{report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_list}"
        )
