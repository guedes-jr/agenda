Claro, aqui está o markdown aprimorado com emojis e badges para melhorar a visualização e tornar o conteúdo mais atrativo:

```markdown
# 📅 Agenda de Eventos

<p align="center">
  <img alt="License" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="150">
</p>

<p align="center">Uma estrutura <a href="https://www.djangoproject.com/" target="_blank">Django</a> criada para realização de agendamento de eventos, contendo um CRUD básico e usando autenticação de usuário.</p>
<p align="center">
   <img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" />
</p>
<p align="center">
  <img alt="License" src="./core/static/img/demo.png">
</p>

# 📑 Índice

1. [🚀 Tecnologias](#tecnologias)
2. [💻 Instalação](#instalação)
3. [🔑 Acesso ao Sistema](#acesso-ao-sistema)
4. [📂 Estrutura do Projeto](#estrutura-do-projeto)
5. [:memo: Licnça](#licença)

## 🚀 Tecnologias

- Django

## 💻 Instalação

1. **Criar um Ambiente Virtual**:

   ```sh
   python -m venv myenv
   ```

2. **Ativar o Ambiente Virtual**:

   - No Windows:
     ```sh
     myenv\Scripts\activate
     ```
   - No Unix ou MacOS:
     ```sh
     source myenv/bin/activate
     ```

3. **Instalar Dependências**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Executar o Projeto**:

   ```sh
   python3 manage.py runserver
   ```

## 🔑 Acesso ao Sistema

Já existe um usuário administrativo `admin` criado no banco de dados do sqlite. Suas credenciais são:

### Usuário Administrador
- **E-mail:** admin@agenda.com
- **Usuário:** admin
- **Senha:** 123456

### Usuário de Testes
- **E-mail:** teste@agenda.com
- **Usuário:** guest
- **Senha:** 123@mudar

### Criar um Novo Usuário Administrativo
```sh
python3 manage.py createsuperuser
```
Também pode acessar o painel administrativo do Django, logar com o admin, acessar os **Usuários** e clicar em **ADICIONAR USUÁRIO**.

## 📂 Estrutura do Projeto

### Apps
- Core

### Rotas
- `admin/`: Painel administrativo do próprio Django
- `agenda/`: Listagem de eventos

## :memo: Licença

Esse projeto está sob a licença MIT.