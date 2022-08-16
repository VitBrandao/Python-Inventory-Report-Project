from collections import Counter


class SimpleReport():
    def get_oldest_date(self, stock):
        oldest_date = stock[0]["data_de_fabricacao"]

        for product in stock:
            if oldest_date > product["data_de_fabricacao"]:
                oldest_date = product["data_de_fabricacao"]

        return oldest_date

    def get_closest_date(self, stock):
        closest_date = stock[0]["data_de_validade"]

        for product in stock:
            if closest_date > product["data_de_validade"]:
                closest_date = product["data_de_validade"]

        return closest_date

    def get_company(self, stock):
        count_companies = list()

        for product in stock:
            count_companies.append(product["nome_da_empresa"])

        counter = Counter(count_companies)
        find_company = max(counter, key=counter.get)
        return find_company

    @classmethod
    def generate(self, stock):
        oldest = self.get_oldest_date(self, stock)
        closest = self.get_closest_date(self, stock)
        company = self.get_company(self, stock)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com mais produtos: {company}"
        )


# object = [
#      {
#        "id": 1,
#        "nome_do_produto": "Joystick",
#        "nome_da_empresa": "Multilaser",
#        "data_de_fabricacao": "2020-08-12",
#        "data_de_validade": "2022-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Manter a temperatura ambiente"
#      },
#      {
#        "id": 2,
#        "nome_do_produto": "Fone de ouvido",
#        "nome_da_empresa": "Multilaser",
#        "data_de_fabricacao": "2021-05-06",
#        "data_de_validade": "2023-03-08",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#      {
#        "id": 3,
#        "nome_do_produto": "Xícara",
#        "nome_da_empresa": "Tramontina",
#        "data_de_fabricacao": "2019-04-12",
#        "data_de_validade": "2020-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Cuidado - frágil"
#      }
#    ]
