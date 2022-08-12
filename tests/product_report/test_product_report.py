from inventory_report.inventory.product import Product


def test_relatorio_produto():
    novo_produto = Product(
        12,
        "Joystick",
        "Multilaser",
        "2022-08-12",
        "2026-08-12",
        "JS48",
        "a temperatura ambiente"
    )

    texto_produto = novo_produto.__repr__()

    # Quebrando string para não comprometer o Flake8
    inicio = "O produto Joystick fabricado em 2022-08-12 por Multilaser "
    meio = "com validade até 2026-08-12 precisa ser armazenado "
    fim = "a temperatura ambiente."

    texto_esperado = inicio + meio + fim

    texto_produto_string = str(texto_produto)

    assert texto_produto_string == texto_esperado
