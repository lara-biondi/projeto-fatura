# projeto-fatura
Anhanguera-Logica-e-Matematica-Computacional-
Título da Apresentação

Simulador de Fatura de Cartão de Crédito

Descrição do Projeto: Este projeto foi solicitado pela professora Maiara Sacramento do 2° Semestre da faculdade Unime Anhanguera do polo Paralela - Salvador Bahia. Foi abordado a possibilidade de criar em três métodos #SouDev, #SouData e #SouSolver.

#SouDev: Implemente um programa que simule a lógica do cartão de crédito, conforme o cenário descrito. O código pode ser feito em qualquer linguagem de programação.

#SouData: Crie um esquema de Banco de Dados que registre as informações sobre as compras, o valor da fatura e a data de pagamento.

#SouSolver: Crie um fluxograma ou diagrama de processos que represente o funcionamento da lógica do pagamento e da cobrança de juros. Isso ajudará os analistas e front-end developers a visualizar o processo.

Sendo assim, para realizar meu projeto optei em realizar como dev back-end, no meu projeto consiste no desenvolvimento de um codigo que simule a lógica de cálculo de uma fatura de cartão de crédito. O sistema permite que o usuário registre múltiplas compras, confira o valor acumulado, defina o dia de pagamento e calcule possíveis juros em caso de atraso no pagamento da fatura que é dia 25. Este simulador foi criado usando a linguagem de Python.

Objetivo

Desenvolver uma aplicação prática que simule a lógica do cálculo de uma fatura de cartão de crédito com juros.Usei com base a ideia que seja pratico para que pessoas com idade ja avançada possam usar. O projeto visa a compreensão e prática de conceitos como:

Acumulação de valores para controle de despesas.
Aplicação de juros com base em um prazo de pagamento.
Manipulação de entradas de dados e exibição dinâmica de resultados.
Criação de uma interface amigável para simulação de um cenário real.
Procedimentos realizados

Registro de Compras: Solicitar o valor de cada compra do usuário, acumulando esses valores na fatura.
Pagamento e Cálculo de Juros: Perguntar o dia do pagamento da fatura e: Caso o pagamento seja até o dia 25, não aplicar juros. Caso o pagamento seja após o dia 25, aplicar uma taxa de 3% sobre o valor total da fatura e mais 1% adicional por dia de atraso após o dia 25.
Exibição de Total Acumulado: Mostrar o valor total acumulado das compras para o usuário.


Demonstração do Funcionamento

Adição de Compras: O usuário insere o valor de cada compra, que é registrado e acumulado. Ao indicar "sim" para a última compra, o sistema desativa a entrada de compras, indicando que o processo pode seguir para o pagamento.

Exibição do Total Acumulado: A cada nova compra, o valor total acumulado é atualizado e exibido automaticamente para o usuário.

Cálculo da Fatura: O usuário insere o dia de pagamento. Caso o pagamento ocorra até o dia 25, o sistema exibe o valor final da fatura sem juros. Se o pagamento ocorrer após o dia 25, o sistema aplica os juros conforme as regras estabelecidas e exibe o valor final da fatura com juros.

Conclusão e Benefícios

Este simulador de fatura de cartão de crédito é um exemplo prático de como conceitos de programação podem ser aplicados para criar uma solução interativa e funcional. A aplicação permite que o usuário compreenda como o atraso no pagamento impacta os juros de uma fatura de cartão de crédito, servindo como uma ferramenta de aprendizado e conscientização sobre a importância do controle financeiro e pagamento em dia.

Essa prática abrange conceitos de programação, estrutura de dados (array de compras), manipulação de DOM, e cálculos financeiros, preparando os desenvolvedores para enfrentar problemas práticos e de relevância cotidiana.
