# 01) O problema de negócio
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes.
Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
Você foi contratado como um Cientista de Dados para criar soluções de dados para entrega, mas antes de treinar algoritmos, a necessidade da empresa é ter um os principais KPIs estratégicos organizados em uma única ferramenta, para que o CEO possa consultar e conseguir tomar decisões simples, porém importantes.
O CEO foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:
## Geral:
1.	Quantos restaurantes únicos estão registrados?
2.	Quantos países únicos estão registrados?
3.	Quantas cidades únicas estão registradas?
4.	Qual o total de avaliações feitas?
5.	Qual o total de tipos de culinária registrados?
## Pais:
1.	Qual o nome do país que possui mais cidades registradas?
2.	Qual o nome do país que possui mais restaurantes registrados?
3.	Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4.	 Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5.	Qual o nome do país que possui a maior quantidade de avaliações feitas?
6.	Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7.	Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8.	Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9.	Qual o nome do país que possui, na média, a maior nota média registrada?
10.	Qual o nome do país que possui, na média, a menor nota média registrada?
11.	Qual a média de preço de um prato para dois por país?
## Cidade:
1.	Qual o nome da cidade que possui mais restaurantes registrados?
2.	Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3.	Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4.	Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5.	Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6.	Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7.	Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8.	Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
## Restaurantes:
1.	Qual o nome do restaurante que possui a maior quantidade de avaliações?
2.	Qual o nome do restaurante com a maior nota média?
3.	Qual o nome do restaurante que possui o maior valor de um prato para duas pessoas?
4.	Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5.	Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6.	Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7.	Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8.	Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
## Culinárias:
1.	Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2.	Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3.	Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4.	Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5.	Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6.	Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7.	Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8.	Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9.	Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10.	Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11.	Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12.	Qual o tipo de culinária que possui a maior nota média?
13.	Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O seu primeiro objetivo como Cientista de Dados é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.
# 02) Premissas assumidas para a análise
1.	Marketplace foi o modelo de negócio assumido.
2.	As três principais visões do negócio foram: Visão países, visão cidades e visão culinária.
# 03) Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa e uma página inicial com os principais indicadores.
1.	Home
2.	Visão do crescimento da empresa.
3.	Visão do crescimento dos restaurantes.
4.	Visão do crescimento dos entregadores.
Cada visão é representada pelo seguinte conjunto de métricas:
## 1.	Home
1.	Quantos restaurantes únicos estão registrados
2.	Quantos países únicos estão registrados
3.	Quantas cidades únicas estão registradas
4.	Qual o total de avaliações feitas
5.	Qual o total de tipos de culinária registrados
6.	Distribuição dos restaurantes por média das avaliações
## 2.	Visão Países
1.	Quantidade de cidades registradas por país.
2.	Quantidade de restaurantes registrados por país.
3.	Relação entre Quantidade de Restaurantes por Cidade nos Paises.
4.	Quantidade Média de Avaliações feitas por País.
5.	Avaliação média e desvio padrão por País.
## 3.	Visão Cidades
1.	Top 10 cidades com mais Restaurantes na Base de Dados.
2.	7 Cidades com média de avaliações acima de 4.
3.	7 Cidades com média de avaliações abaixo de 2.5.
4.	Top 10 Cidades com mais restaurantes com tipos culinários distintos.
## 4.	Visão Culinária

1.	Nome e maior avaliação média dos restaurantes que possuem o tipo de culinária italiana, americana, árabe, japonesa e brasileira.
2.	Top 10 melhores tipos de culinárias.
3.	Top 10 piores tipos de culinárias.

# 04) Insights de dados
1.	40% das cidades e 44% dos restaurantes estão localizadas na Índia.
2.	Brasil, Inglaterra e África do Sul possuem a maior concentração de restaurante por cidade e esses países possuem as cidades com melhores médias de avaliações.
3.	As cidades da Inglaterra possuem a maior variedade de tipos de culinária.
# 05) O produto final do projeto
O painel online, hospedado em um Cloud, disponível para acesso em qualquer dispositivo conectado à internet pode ser acessado através do link: https://fome-zero-lucasdepaulacds-ftc.streamlit.app/

# 06) Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e tabelas que exibam essas métricas da melhor forma possível para o CEO.
# 07) Próximos passos
1.	Reduzir o número de métricas.
2.	Criar novos filtros.
3.	Adicionar novas visões de negócio.
