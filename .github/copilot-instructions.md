# Instruções do Projeto

Este repositório contém um portal educacional estático para compartilhar tarefas e exercícios de programação com alunos. Os alunos devem conseguir navegar pelas atividades, consultar seus detalhes e baixar os arquivos fornecidos.

## Estrutura

- `index.html` é a página principal do portal.
- `config.json` fornece os dados do curso e a lista de atividades exibida no site.
- `assignments/` contém uma subpasta por atividade, com instruções e, quando aplicável, arquivos iniciais e materiais de apoio.
- `templates/assignment-template.md` é o modelo para criar instruções de novas atividades.
- `assets/` contém os estilos, scripts, imagens e outros recursos do site.

## Diretrizes de implementação

- Mantenha o site estático e siga os padrões de HTML, CSS e JavaScript já utilizados no projeto.
- Preserve o estilo visual e a navegação existentes; prefira alterações pequenas e consistentes.
- Ao adicionar ou alterar uma atividade, mantenha `config.json` e os arquivos da pasta correspondente sincronizados. Use um `id` único e caminhos relativos válidos para pastas e anexos.
- Para novas atividades, siga a estrutura do `templates/assignment-template.md` e mantenha os arquivos de cada atividade em sua própria subpasta de `assignments/`.
- Use nomes de arquivos e pastas descritivos, e não adicione dependências ou ferramentas sem necessidade.

## Conteúdo educacional

- Escreva instruções claras, acolhedoras e adequadas ao nível de dificuldade da atividade.
- Defina objetivos de aprendizagem concretos e requisitos verificáveis para cada tarefa.
- Inclua exemplos ou arquivos iniciais quando ajudarem o aluno a começar, sem remover a oportunidade de praticar os conceitos ensinados.
- Mantenha o idioma consistente com o conteúdo existente na atividade que estiver sendo editada.
