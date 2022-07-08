- - -
Title: Permissões Date: 2021-04-18 Order: 2
- - -

O acesso do usuário às diferentes funções do serviço é controlado pelo [sistema nativo de autenticação](https://docs.djangoproject.com/en/3.2/topics/auth/default/) do Django. Quando uma instância é criada, o script `initdb` cria um conjunto de permissões que são atribuídas a grupos. Por padrão, todos os novos usuários são colocados no grupo `editor`, que permite que eles editem metadados de livros.

A pessoa que administra a instância deve ser do grupo `superuser`, que dá a ela acesso à administração do Django (`/admin`) e a todas as permissões.

## Permissões e grupos
Esta tabela mostra os quatro grupos (admin, moderador, editor e usuário) e que permissões usuários nesses grupos têm:

|                                   | administrador | moderador | editor | usuário |
| --------------------------------- | ------------- | --------- | ------ | ------- |
| editar configurações da instância | ✔️            | -         | -      | -       |
| mudar nível do usuário            | ✔️            | -         | -      | -       |
| gerir federação                   | ✔️            | ✔️        | -      | -       |
| enviar convites                   | ✔️            | ✔️        | -      | -       |
| desativar usuários                | ✔️            | ✔️        | -      | -       |
| excluir publicações               | ✔️            | ✔️        | -      | -       |
| editar livros                     | ✔️            | ✔️        | ✔️     | -       |
 enviar capas            |  ✔️    |     ✔️       |   ✔️     |  ✔️
