# Boas-vindas ao repositório do Inventory Reports
---

# Requisitos obrigatórios

## 1 - Testar o construtor/inicializador do objeto Produto
> **Crie o teste em:** tests/product/test_product.py

Ao analisar o código do projeto, você encontrará a classe do objeto produto já implementada neste arquivo: `inventory_report/inventory/product.py`, a classe **Product**.

Para termos confiança em continuar as implementações, precisamos que você implemente o teste, que certifique que o método `__init__` da classe Product esta funcionando corretamente.

O nome deste teste deve ser `test_cria_produto`, ele deve verificar o correto preenchimento dos seguintes atributos:
  - id (int)
  - nome_da_empresa (string)
  - nome_do_produto (string)
  - data_de_fabricacao (string)
  - data_de_validade (string)
  - numero_de_serie (string)
  - instrucoes_de_armazenamento (string)

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **1** - Deve criar um novo produto com todos os atributos corretamente preenchidos.

</details>

<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendindo quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>


## 2 - Testar o relatório individual do produto
> **Crie o teste em:** tests/product_report/test_product_report.py

Boa novidade, o primeiro relatório já implementamos neste arquivo `inventory_report/inventory/product.py`. Formulamos uma frase construída com as informações do produto, que será muito útil para etiquetarmos o estoque.

Para desenvolver este relatório, utilizamos o recurso `__repr__` do Python, que permite alterar a representatividade do objeto, para que sempre que usarmos um print nele, no lugar de endereço de memória, teremos uma String personalizada. 

**Dica:** A reimplementação do `__repr__` não faz o objeto retornar exatamente uma `string`, fazer um `cast` para `string`, pode te ajudar.

Exemplo da frase:
> O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.

Agora para mantermos uma boa cobertura de testes, precisamos que você implemente o teste.

O nome deste teste deve ser `test_relatorio_produto`, ele deve instanciar um objeto `Product` e verificar se acessá-lo a frase de retorno esta correta.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


  - **1** - Se seu código testa que o retorno padrão (`__repr__`) de um objeto `Product` deve ser um relatório sobre ele 
</details>
    
<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendindo quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>


## 3 - Gerar a versão simplificada do relatório

> **Crie a classe em:** inventory_report/reports/simple_report.py

O relatório deve ser gerado através de um método de classe chamado `generate` escrito dentro da classe `SimpleReport`.

- Ao rodar os testes localmente, você terá um teste para cada validação de cada informação
- Deve ser possível executar o método `generate` sem instanciar um objeto de `SimpleReport`
- O método deve receber um parâmetro que representa uma `list` (estrutura de dados), onde cada posição contém um `dict`(estrutura de dados).

Exemplo de formato de entrada

```json
   [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]
```

- O método deverá retornar uma `string` de saída com o seguinte formato:
   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com mais produtos: NOME DA EMPRESA
   ```
- A data de validade mais próxima, somente considera itens que ainda não venceram.

**Dica:** O módulo [datetime](https://docs.python.org/3/library/datetime.html) pode te ajudar.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


  - **3.1** - O método generate da classe SimpleReport deve retornar todas informações do relatório simples. Informações necessárias:
    - a data de fabricação mais antiga
    - a validade mais próxima
    - a empresa com maior número de produtos

  - **3.2** - O método generate da classe SimpleReport deve retornar o formato correto do relatório simples

    📌 Atente-se a espaçamentos e quebras de linhas

</details>

## 4 - Gerar a versão completa do relatório

> **Crie em:** inventory_report/reports/complete_report.py

O relatório deve ser gerado através de um método `generate` para a classe `CompleteReport`.
Ele deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- A classe `CompleteReport` deve herdar o método (`generate`) da classe `SimpleReport`, de modo a especializar seu comportamento.

- Deve ser possível executar o método `generate` sem instanciar um objeto de `CompleteReport`
  
- O método deve receber de parâmetro uma lista de dicionários no seguinte **formato**:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "MESA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-05-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


  - **2.1** - O método generate da classe CompleteReport deve retornar todas informações do relatório completo no formato correto. Informações necessárias:
    - a data de fabricação mais antiga
    - a validade mais próxima
    - a empresa com maior estoque
    - a quantidade de produtos por empresa, ordenado pela mesma ordem que as empresas aparecem na lista de entrada

</details>

## 5 - Gere os relatórios através de um arquivo CSV
> **Crie em:** inventory_report/inventory/inventory.py

A importação do arquivo CSV deve ser realizada através do método `import_data` que você deve criar em uma classe chamada `Inventory`.
    
O método deve ser estático ou de classe, ou seja, deve ser possível chamá-lo sem instanciar um objeto da classe.

O método receberá como primeiro parâmetro uma string como caminho para o arquivo `CSV` e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **3** - Ao importar um arquivo CSV, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>

## 6 - Gere os relatórios através de um arquivo JSON
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.

Altere o método `import_data` para que ele também seja capaz de carregar arquivos `JSON`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- **4** - Ao importar um arquivo JSON, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>

## 7 - Gere os relatórios através de um arquivo XML
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.
    
Altere o método `import_data` para que ele também seja capaz de carregar arquivos `XML`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>
  
  - **5** - Ao importar um arquivo XML, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>
