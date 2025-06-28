# CRUD de Produtos em Python com MySQL

Este projeto é um sistema de cadastro de produtos (CRUD) utilizando Python e MySQL. Ele permite cadastrar, listar, atualizar, deletar produtos e reiniciar a tabela de vendas, tudo via terminal.

## Funcionalidades

- **Cadastrar produto:** Adiciona um novo produto com nome e valor.
- **Listar produtos:** Exibe todos os produtos cadastrados.
- **Atualizar produto:** Permite alterar o nome ou valor de um produto, buscando por ID, nome ou valor.
- **Deletar produto:** Remove um produto do banco de dados por ID, nome ou valor.
- **Reiniciar tabela:** Apaga todos os registros e reinicia o contador de IDs.
- **Sair:** Encerra o programa.

## Pré-requisitos

- Python 3
- MySQL Server
- Biblioteca `mysql-connector-python`



## Como usar

1. Execute o arquivo `python.py`:
    ```
    python python.py
    ```

2. Siga as instruções do menu para realizar as operações desejadas.

## Observações

- Todos os dados são armazenados na tabela `vendas` do banco `bdyoutube`.
- A opção de reiniciar a tabela apaga todos os produtos e reinicia o contador de IDs.
- Use as opções de atualização e exclusão com atenção, pois as operações são permanentes.

---

Desenvolvido para fins educativos
