<h1 align="center">Boas-vindas ao repositório do Job Insights!</h1>
<br />

## Objetivo

O <strong>Job Insights</strong> tem como objetivo desenvolver soluções de análises de dados reais sobre empregos. As implementações foram incorporadas a um aplicativo web desenvolvido com flask já disponibilizado no projeto.

## O que foi desenvolvido?

O <strong>Job Insights</strong> é um projeto desenvolvido em python e a principal finalidade foi realizar a manipulação e extração de dados sobre empregos: quais empregos existem na base de dados, quais as indústrias estão presentes, obter salário máximo e mínimo, filtrar o emprego pelo seu tipo e indústria e por fim filtrar o salário por um determinado intervalo. Esse projeto foi ótimo para praticar alguns conhecimentos sobre python: utilizar o terminal interativo do python,
utilizar estruturas condicionais e de repetição, utilizar funções built-in do python, utilizar tratamento de exceções, realizar a manipulação de arquivos, escrever funções, escrever testes com pytest e escrever meus próprios módulos e importá-los em outros códigos.

## Linguagens e ferramentas
- Python
- Flask
- Pytest

## Instalação e execução

### 1 - Clone o repositório:

```
git clone git@github.com:h3zord/job-insights.git
```

### 2 - Entre no repositório:
```
cd job-insights
```

### 3 - Crie um ambiente virtual:
```
python3 -m venv .venv && source .venv/bin/activate
```

### 4 - Instale as dependências no ambiente virtual:
```
python3 -m pip install -r dev-requirements.txt
```

### 5 - Inicie a aplicação:
```
flask run
```

<strong>A aplicação vai rodar na porta 5000</strong>
<br/>
➜ http://localhost:5000/

<br/>

## Execução dos testes

### 1 - Rode o comando:
```
python3 -m pytest
```