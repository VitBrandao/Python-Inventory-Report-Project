from inventory_report.inventory.product import Product


def test_cria_produto():
    novo_produto = Product(
        12,
        "Joystick",
        "Multilaser",
        "2022-08-12",
        "2026-08-12",
        "JS48",
        "Manter a temperatura ambiente"
    )

    assert novo_produto.id == 12
    assert novo_produto.nome_do_produto == "Joystick"
    assert novo_produto.nome_da_empresa == "Multilaser"
    assert novo_produto.data_de_fabricacao == "2022-08-12"
    assert novo_produto.data_de_validade == "2026-08-12"
    assert novo_produto.numero_de_serie == "JS48"

    instrucao = "Manter a temperatura ambiente"
    assert novo_produto.instrucoes_de_armazenamento == instrucao
