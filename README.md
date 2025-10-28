# Projeto-Pim-BIM1-2

Usaremos aqui como registro para saber oque temos feito até o momento:

<h2>Pendentes:</h2>

- CRUD Turma
- Login Aluno
- ChatBot
- Login Administrador com CRUD para (Turmas, Professor e Alunos)

<h2>Cadastro Professor(CRUD)</h2>

<b>Responsavel: Reinaldo<br></b>
- Tarefa Atual: Login Professor<br>
Stiuação: Em andamento

Ultima atualização: 21/10

Objetivos:

- CRUD Material
- CRUD Atividade
- CRU Nota

Alcançados:

- Cadastro professor<br>
Obs: Estou fazendo algumas implementações necessarias ao professor, como conferir CPF, conferir telefone, email, os principais se turma e curso existem no sistema, serão as proximas atualizações que serão feitas a ele. Estou ajustando por enquanto esses dados pois quando for fazer o alterar sera mais simples pra puxar os dados, e as funções necessarias para conferir os dados corretos.

Devo deixar o CPF sempre como "apenas se existir a partir do calculo" ou qualquer cpf que não contenha letras e caracters especiais? Estou disponivel para duvidas quaisquer.

(Henrique Respondendo): Por mim acho que não precisaria ter essa métrica não. Vai acbar nos dando mais trabalho, então acho que apenas ter o número exato de caracteres de um cpf de verdade já é o suficiente, pra simplificar nossa vida.

<h2>Cadastro Aluno(CRUD)</h2>

<b>Responsavel: Henrique<br></b>
- Tarefa Atual: Login Alunos<br>
Stiuação: Em Andamento (quase concluída)

Ultima atualização: 27/10

Objetivos:

- Responder Atividade
- Ler Atividade
- Consultar Material
- Consultar Nota

Alcançados:

- Cadastro Alunos<br>
Obs:
(21/10) Ainda preciso adicionar alguns atributos nos dicionários, mas em geral tem ocorrido bem. Separei os métodos "dump" e "load" em funções
pra ficar organizado, e usei o "import os" pra mexer com o funcionamento do sistema, qualquer dúvida sobre isso podem me perguntar. Em breve farei mais atualizações para finalizar essa etapa.
(22/10) Apliquei os atributos que faltavam aos usuários, e adicionei mais duas funcionalidades: deletar_usuário() e modificar_usuario(), com isso o CRUD de alunos está completo. Talvez ainda possa fazer algumas modificações, como fazer com que todas as respostas inseridas nos "inputs" fiquem minúsculas (sugestão do Reinaldo), ou alguma observação que vocês vierem a fazer (To pensando em mexer um pouco no design que aparece no terminal, mas daí é bom conversarmos todos para chegarmos a um padrão).
(24/10) Criei as funções de verificação para cada tipo de dado de cadastro dos alunos, menos RA, endereço e curso. Endereço porque basicamente não tem limitações de caracteres, RA porque eu ainda preciso criar uma função que gera automaticamente um RA e o atribui aos alunos (tipo um id), e cursos porque ainda não temos os cursos pré-definidos na plataforma, então não dá pra filtrar nada, temos que ver isso. A interface vou ver de postar ainda hoje, apenas o protótipo com as rotinas do usuário. Obs: Meu código já ultrapassou as 200 linhas e eu nem acabei kkkkk, espero q n dê problema na hora de imprimir isso. (27/10) Implementei um recurso dentro da função "cadastrar_novo_aluno", que gera um RA de 7 digitos, com 5 letras maiusculas e 2 numeros de 0 a 9. Também retirei o atributo de "endereço" dos alunos e modifiquei alguns detalhes na estrutura do projeto, para que ele funcionasse corretamente. Criei o primeiro protótipo da interface do site pros alunos, que contém todos os métodos citados no diagrama de classes, e que já possui ligação direta com o a lista.JSON que contém os cadastros dos alunos salvos, só precisaria ter uma ligação com o código da parte dos professores, para que as opções "Consultar Notas", "Consultar Atividades" e "Consultar Material" funcionem, isso daí vemos depois. Diria que já estou nas etapas finais, esse projeto ta ficando top demais slk. (28/10) Hoje complementei o cadastro de alunos, colocando opções de cancelar alguma ação não intencional por parte do usuário, criei uma função que impede dois dados iguais existirem no banco de dados, aplicada para os atributos "email", "telefone" e "CPF", criei o atributo "sobrenome" pros alunos, e comentei boa parte do código que acho que já seja o suficiente. 

<h2>Cadastro Cursos(CRUD)</h2>

<b>Responsavel: Natan<br></b>
- Tarefa Atual: <br>
Stiuação: 

Ultima atualização: 

Objetivos:


Alcançados:
