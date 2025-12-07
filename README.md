Desenvolvimento de Sistema Web para Gerenciamento de Veículos:
Implementação de CRUD com Python Flask e SQLite


Acadêmico – Cláudio Gabriel Bastos Rangel
Turma – FLD6661946CET
Tutor – Márcio Poffo 



RESUMO 

Fiz esse projeto para gerenciar veículos pela web. Usei Python com Flask e um banco de dados SQLite simples. A ideia principal era criar um sistema que fizesse o básico: cadastrar, ler, atualizar e apagar informações de carros (CRUD).
Trabalhei passo a passo. Primeiro, organizei como os dados seriam salvos. Depois, programei as funções que fazem o sistema funcionar por trás (o backend) e, por fim, montei a parte visual que o usuário vê, tentando deixar a interface fácil de usar em qualquer aparelho (responsiva).
No sistema, dá para incluir dados importantes de cada veículo, como modelo, marca, ano e uma descrição. Você pode ver todos os registros, mudar as informações se precisar e apagar os que não servem mais.
No fim, consegui uma aplicação web que funciona bem e é fácil de usar. O projeto mostra como essas ferramentas (Python, Flask, SQLite) podem ser úteis para criar sistemas de gerenciamento e controle de estoque simples para empresas pequenas.




INTRODUÇÃO 

A necessidade de sistemas digitais para controle de patrimônio automotivo. O problema visto é identificado que um vendedor por ter um número grande de veículos, uma página com todas informações pode facilitar a sua consulta de estoque. Com esse sistema CRUD, reforcei meu conhecimento em rotas e gerenciamento de banco de dados. 

 








FUNDAMENTAÇÃO TEÓRICA 
Figura 1 - Implementação do Modelo de Dados com SQLAlchemy ORM

A Figura 1 demonstra a implementação do modelo de dados utilizando SQLAlchemy ORM, onde a classe Item herda de db.Model e define a estrutura da tabela de veículos. 
Copeland (2008) define SQLAlchemy como "a ferramenta mais poderosa e flexível para trabalhar com bancos de dados relacionais em Python", característica evidenciada na simplicidade da definição de campos através de db.Column, que abstrai completamente a sintaxe SQL subjacente. O ORM permite que desenvolvedores trabalhem com objetos Python ao invés de escrever comandos SQL diretamente, aumentando produtividade e reduzindo erros de programação.

Figura 2 - Implementação da Operação CREATE do CRUD

A Figura 2 apresenta a implementação da operação CREATE no sistema desenvolvido, demonstrando como dados do formulário web são processados e persistidos no banco de dados. Date (2003) estabelece que "estas operações formam a base de qualquer sistema de banco de dados prático", princípio aplicado na função create() que recebe dados via método POST, instancia um novo objeto Item e utiliza db.session.add() seguido de db.session.commit() para efetivar a inserção. Esta abordagem exemplifica a integração entre framework Flask e SQLAlchemy para manipulação de dados de forma segura e eficiente.


Figura 3 - Organização do Projeto Seguindo o Padrão MVC

A Figura 3 ilustra a estrutura organizacional do projeto baseada no padrão Model-View-Controller (MVC), que separa responsabilidades em três camadas distintas. Fowler (2002) explica que "MVC promove separação de responsabilidades, facilitando manutenção e evolução do software", arquitetura implementada através da divisão em: models.py responsável pela definição de estruturas de dados (Model), routes.py contendo a lógica de controle e processamento de requisições (Controller), e o diretório templates/ abrigando as interfaces HTML apresentadas ao usuário (View). Essa organização resulta em código mais limpo, organizado e facilita futuras expansões do sistema.




METODOLOGIA 

A metodologia adotada foi o desenvolvimento incremental orientado a funcionalidades,
seguindo as seguintes etapas:

Método de Pesquisa: Pesquisa aplicada com base na documentação oficial das
tecnologias utilizadas.

Abordagem: Qualitativa, focada na implementação prática dos conceitos estudados.

Tipo de Pesquisa: Bibliográfica e experimental, baseada em documentação técnica
e testes práticos.

Instrumentais Utilizados:
- Documentação oficial do Python Flask
- Tutoriais de SQLite
- Guias de Bootstrap CSS
- Editor de código VS Code
- Navegador web para testes

Etapas de Desenvolvimento:
1. Análise dos requisitos do sistema
2. Modelagem do banco de dados
3. Configuração do ambiente de desenvolvimento
4. Implementação dos modelos de dados (models.py)
5. Desenvolvimento das rotas e lógica de negócio (routes.py)
6. Criação das interfaces web (templates HTML)
7. Aplicação de estilos CSS com Bootstrap
8. Testes funcionais das operações CRUD
9. Documentação do código

Fonte das Informações: Documentações oficiais das tecnologias, artigos técnicos
e manuais de boas práticas em desenvolvimento web.


CONSIDERAÇÕES 

Objetivos Alcançados: Sistema funcional com todas as operações CRUD implementadas
Aprendizados Técnicos: Domínio do Flask, SQLite e desenvolvimento web
Desafios Enfrentados: Configuração do ambiente, estruturação do projeto
Aplicabilidade Prática: Uso real em pequenas empresas ou oficinas
Possíveis Melhorias: Autenticação de usuários, relatórios, backup automático e listas de clientes.




REFERÊNCIAS BIBLIOGRÁFICAS 

COPELAND, Rick. Essential SQLAlchemy. Sebastopol: O'Reilly Media, 2008.

DATE, C. J. An Introduction to Database Systems. 8ª ed. Boston: Addison-Wesley, 2003.

FOWLER, Martin. Patterns of Enterprise Application Architecture. Boston: Addison-Wesley, 2002.

FLASK DEVELOPMENT TEAM. Flask Documentation. Disponível em: https://flask.palletsprojects.com/. Acesso em: 07 dez. 2025.

PYTHON SOFTWARE FOUNDATION. Python 3 Documentation. Disponível em: https://docs.python.org/3/. Acesso em: 07 dez. 2025.

SQLITE CONSORTIUM. SQLite Documentation. Disponível em: https://www.sqlite.org/docs.html. Acesso em: 07 dez. 2025. 
