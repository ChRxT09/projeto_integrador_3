# Scripts

listagem de scripts executáveis com o `make`:

| Comando               | Descrição                                                                            |
| --------------------- | ------------------------------------------------------------------------------------ |
| `correct`             | converte o arquivo de LATIN1 para UTF-8                                              |
| `download`            | Faz o download dos arquivos (alguns esão comentados pois serão tratados futuramente) |
| `python_requirements` | instala as dependêcias necessárias do python                                         |
| `staging_area`        | importará o csv para o banco por meio do psql                                        |
| `prepare_database`    | Prepara o banco de dados com o schema do prisma                                      |
| `prepare_project`     | Prepara o prisma para ser executado                                                  |
| `star`                | insere os dados nas tabelas fato e dimensão                                          |
| `etl`                 | executa os comandos acima na ordem correta                                           |

Para executar um comando utilizando o `GNU make`, basta digitar no terminal, diretório raiz do projeto:
``` bash
make [comando]
```