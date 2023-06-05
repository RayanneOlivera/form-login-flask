def valida_cadastro(nome, email, senha, confsenha):
    # Verifica se o campo nome está vazio
    if nome == '':
        return 'O campo nome é obrigatório'

    # Verifica se o nome tem menos de 3 caracteres
    elif len(nome) < 3:
        return 'O nome deve ter pelo menos 3 caracteres'

    # Verifica se o campo email está vazio
    elif email == '':
        return 'O campo e-mail é obrigatório'

    # Verifica se o campo senha está vazio
    elif senha == '':
        return 'O campo senha é obrigatório'

    # Verifica se a senha é diferente da confirmação de senha
    elif senha != confsenha:
        return 'As senhas não conferem'

    # Caso todas as verificações passem, retorna None
    else:
        return None
