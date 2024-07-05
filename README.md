# Agenda de Evendos

[circleci-url]: https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg

  <p align="center">Uma estrutura <a href="https://www.djangoproject.com/" target="_blank">Django</a> progressiva para criar aplicativos do lado do servidor eficientes e escalonáveis.</p>
    <p align="center">
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/v/@nestjs/core.svg" alt="NPM Version" /></a>
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" /></a>
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/dm/@nestjs/common.svg" alt="NPM Downloads" /></a>
<a href="https://circleci.com/gh/nestjs/nest" target="_blank"><img src="https://img.shields.io/circleci/build/github/nestjs/nest/master" alt="CircleCI" /></a>
<a href="https://coveralls.io/github/nestjs/nest?branch=master" target="_blank"><img src="https://coveralls.io/repos/github/nestjs/nest/badge.svg?branch=master#9" alt="Coverage" /></a>
<a href="https://discord.gg/G7Qnnhy" target="_blank"><img src="https://img.shields.io/badge/discord-online-brightgreen.svg" alt="Discord"/></a>
<a href="https://opencollective.com/nest#backer" target="_blank"><img src="https://opencollective.com/nest/backers/badge.svg" alt="Backers on Open Collective" /></a>
<a href="https://opencollective.com/nest#sponsor" target="_blank"><img src="https://opencollective.com/nest/sponsors/badge.svg" alt="Sponsors on Open Collective" /></a>
  <a href="https://paypal.me/kamilmysliwiec" target="_blank"><img src="https://img.shields.io/badge/Donate-PayPal-ff3f59.svg"/></a>
    <a href="https://opencollective.com/nest#sponsor"  target="_blank"><img src="https://img.shields.io/badge/Support%20us-Open%20Collective-41B883.svg" alt="Support us"></a>
  <a href="https://twitter.com/nestframework" target="_blank"><img src="https://img.shields.io/twitter/follow/nestframework.svg?style=social&label=Follow"></a>
</p>

## Tecnologias:

- Django

## Instalação

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
4. **Executar projeto**

```sh
python3 manage.py runserver
```

## Acesso ao Sistema

Já existe um usuário administrativo `admin` criado no bando de dados do sqlite.
Sua credências são:

### Usuário administrador
- **E-mail:** admin@agenda.com
- **Usuário:** admin
- **Senha:** 123456

### Usuário de testes
- **E-mail:** teste@agenda.com
- **Usuário:** guest
- **Senha:** 123@mudar

### Criar um novo usuário adminitrativo
```sh
python3 manage.py createsuperuser
```
Também pode estar acessando o painel administrativo do django, logar com o admin, acessar os **Usuários** e clicar em **ADICIONAR USUÁRIO**.
## Estrutura do Projeto
### Apps
   - Core

### Rotas
   - `admin/`: Painel administrativo do próprio Django
   - `agenda/`: Listagem de eventos