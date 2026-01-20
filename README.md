Sistema de Classificação de Plantas Brasileiras

Projeto Final – Programação Orientada a Objetos (POO)
Universidade Federal do Ceará (UFC) – 2025.2

⸻

📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema em Python para identificação e classificação de plantas representativas do Brasil, utilizando os princípios da Programação Orientada a Objetos (POO).

O sistema foi idealizado a partir de um contexto proposto em sala de aula, no qual o desenvolvedor atua como um especialista em botânica e sistemas, contratado por uma ONG ambiental, com o objetivo de facilitar a identificação de plantas com base em características botânicas padronizadas, amplamente utilizadas pela comunidade científica.

A classificação das plantas ocorre por meio de perguntas interativas, permitindo identificar corretamente os seguintes grupos botânicos:
	•	Briófitas (Musgos)
	•	Pteridófitas (Samambaias)
	•	Gimnospermas
	•	Angiospermas

⸻

🎯 Objetivos
	•	Aplicar corretamente os pilares da Programação Orientada a Objetos
	•	Modelar um problema real por meio de classes e subclasses
	•	Desenvolver um sistema organizado em múltiplos módulos
	•	Criar um menu interativo para identificação de plantas
	•	Facilitar a compreensão da classificação botânica por meio de software

⸻

🧠 Conceitos de Programação Orientada a Objetos Aplicados

O projeto contempla explicitamente os quatro pilares da Programação Orientada a Objetos:

🔹 Abstração

A classe Planta representa o conceito genérico de uma planta, contendo atributos e comportamentos comuns a todos os tipos.

🔹 Encapsulamento

Os atributos da classe Planta são protegidos por convenção (uso de _atributo), garantindo maior controle sobre os dados internos dos objetos.

🔹 Herança

As classes especializadas herdam atributos e métodos da classe base Planta, evitando repetição de código e promovendo reutilização.

🔹 Polimorfismo

O método exibir_info() é sobrescrito nas subclasses, permitindo comportamentos distintos para cada tipo de planta, mesmo sendo chamado de forma uniforme.

⸻

🗂️ Estrutura do Projeto
📁 projeto-plantas
│
├── planta.py          # Superclasse Planta
├── sem_flores.py      # Classes de plantas sem flores
├── com_flores.py      # Classes de plantas com flores
├── main.py            # Arquivo principal (menu e execução)
├── README.md          # Documentação do projeto


Modelagem das Classes

Hierarquia de Classes (Resumo)
Planta
 ├── PlantaSemFlores
 │     ├── Musgo
 │     └── Samambaia
 └── PlantaComFlores
       ├── Gimnosperma
       └── Angiosperma

Descrição das Classes
	•	Planta: classe base com atributos e métodos comuns
	•	PlantaSemFlores: representa plantas sem flores e sementes
	•	PlantaComFlores: representa plantas com flores e sementes
	•	Musgo: briófita
	•	Samambaia: pteridófita
	•	Gimnosperma: planta com sementes, porém sem fruto
	•	Angiosperma: planta com sementes e fruto

⸻

▶️ Funcionamento do Sistema

Ao executar o sistema, o usuário visualiza um menu interativo:
SISTEMA DE CLASSIFICAÇÃO DE PLANTAS
1 - Identificar uma planta
0 - Sair


Ao selecionar a opção de identificação, o sistema realiza perguntas como:
	•	A planta possui flores?
	•	Possui vasos condutores (raiz, caule e folhas)?
	•	Possui frutos?
	•	Tipo de angiosperma (monocotiledônea ou dicotiledônea)

Com base nas respostas fornecidas, o sistema identifica automaticamente a classe correta da planta e exibe suas informações.

⸻

📸 Evidências de Execução

Durante os testes do sistema, foram realizadas:
	•	Execução do menu principal
	•	Identificação de plantas com e sem flores
	•	Exibição correta das classificações botânicas

Prints da execução podem ser adicionados conforme solicitado no enunciado do projeto.

⸻

📊 Considerações Finais

O sistema atende integralmente aos requisitos propostos no Projeto Final da disciplina de Programação Orientada a Objetos, apresentando:
	•	Organização adequada do código
	•	Uso correto dos conceitos de POO
	•	Interação clara com o usuário
	•	Modelagem coerente do domínio botânico escolhido

Além disso, o projeto possui estrutura modular, facilitando futuras expansões, como a inclusão de novos tipos de plantas ou critérios adicionais de classificação.
