# Agenda de Evendos

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

## Usuário admin

Já existe um usuário admin criado no bando de dados do sqlite.
Sua credências são:

- **E-mail:** admin@agenda.com
- **Usuário:** admin
- **Senha:** 123456

## Estrutura do Projeto
### Apps
   - Core

### Rotas
   - `admin/`: Painel administrativo do próprio Django
   - `agenda/`: Listagem de eventos