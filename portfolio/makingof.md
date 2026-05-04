# Entidades

----
## Licenciatura
    
- Universidade (nome)
- Nome
- Abreviatura
- Duração (em anos)

### Relações
>Unidades Curriculares **N** <-> **N**

---
## Unidade curricular

- Nome
- Abreviatura
- Ano (dentro da licenciatura);
- Semestre (1 ou 2);

### Relações

>Licenciatura **1** <-> **N**<br>
> Tecnologia - **N** <-> **N**
> 
---
## Projeto

- Nome
- Descrição

### Relações

>Tecnologia - **N** <-> **N**<br>
>Unidade Curricular - **N** <-> **N**<br>
>Competencia - **N** <-> **N**

## Tecnologia

- Nome
- Areas (ex: backend, base de dados, etc.)
- Descrição

### Relaçṍes
> Unidade Curricular - **N <-> N**<br>
> Contribuição Open-Source - **N** <-> **N**<br>
> Projeto - **N** <-> **N**
---
## Competencia

- Nome
- Descrição

### Relações
> Projeto - **N** <-> **N** <br>
> Formação - **N** <-> **N**
---
## Formação

- Titulo
- Descrição
- Data

### Relações
> Competencia - **N** <-> **N**
---
## Contribuições Open-Source

- Nome do Projeto
- Descrição projeto
- Descrição da minha contribuição
- Link para repositorio do projeto

### Relações
> Tecnologia - **N** <-> **N**

---

## TFC

- Titulo
- Descrição
- Rating
- Autores
- Orientadores
- Tecnologias
- Areas
- Pdf
- Imagem
- KeyWords

--- 

## Modelo ER

![Foto do modelo](/media/modelação.png)

---

# Lab 7

*Fora pedido que fizemos para cada modelo do nosso portfolio uma view, um template e a respectiva url.*

---

# Lab 8

Ainda não havia inserido dados nenhum a minha base de dados (a nível do portfolio), exceto os tfcs que foram pedidos. Então aproveitei para inserir dados agora.

Após inserir os dados que considerei relevantes passei a criação dos formulários.

## Formulários

> Fora pedido que criassemos formularios para criar, editar e apagar os modelos <u>Projeto</u>, <u>Tecnologia</u>, <u>Competencia</u> e <u>Formação</u>.



