# Projeto Integrador III

Grupo 3:

- [Gustavo de Oliveira Christ](https://github.com/ChRxT09) (Ciência da Computação)
- [Jhony Rodrigues de Souza](https://github.com/jhonyrdesouza) (Sistemas de Informação)
- [Lúcio Ewald do Nascimento](https://github.com/lucioew28) (Ciência da Computação)
- Esdras dos Reis Souza
- Lucas Rodrigues da Cruz

## Sobre o Projeto

TODO

## Preparando o ambiente

### Tecnologias utilizadas

O projeto utiliza de váras tecnologias, dentre elas:

- Python: realização de consultas e inserção de dados com o auxílio das
  seguintes bibliotecas:
  1. Pandas: utilizado para fazer a análise de dados;
  2. psycopg2: Utilizadso para conectar com o banco de dados;
- pip: gerenciador de pacotes do Python;
- GNU make: automação de processos;
- Prisma: ORM baseado em Javascript, utilizado para a modelagem do banco
  de dados;
- yarn: gerenciador de pacotes Javascript, utilizado em conjunto com o
  prisma para a criação e aplicação de Migrations;
- psql: cliente do Postrgresql, usado para a importação do csv para
  o banco de dados;

### Instalação do GNU make

Para instalar o GNU make, utilize as seguintes linhas de comando no
terminal:

```bash
sudo apt update && sudo apt upgrade
sudo apt install make -y
```

### Preparando o Prisma

crie um arquivo `.env` no diretório `db/prisma` ou, se preferir, copie e
cole o arquivo `env.example`, renomeie-o para `.env` e insira o link
do banco de dados, seguindo a estrutura proposta.

### Inserindo os dados no banco

Com o GNU make instalado, basta executar, no temrinal, a seguinte linha de comando:

```bash
make etl
```

esse comando pode ser dividido em cinco etapas:

- Prepara o banco de dados;
- Baixa o arquivo .csv;
- Corrige o arquivo e sua estrutura;
- importa os dados para a staging area;
- transformação e carga.

