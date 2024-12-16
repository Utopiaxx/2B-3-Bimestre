#miguel andrade
#informatica 2 V

def registrar_usuario():
    try:
        tipo = input("Tipo de usuário:\n\n1 - Aluno\n2 - Visitante\n3 - Chefe De Departamento\nEscolha o seu tipo de usuário: ").strip()
        print("\nRegistrar informações\n")
        nome = input("Digite seu nome completo: ").strip()
        cpf = input("Digite seu CPF: ").strip()
        idade = input("Digite sua Idade: ").strip()
        senha = input("Digite sua senha: ").strip()

        if any(usuario.cpf == cpf for usuario in usuarios):
            raise UsuarioJaCadastradoError("Erro: Pessoa já cadastrada.")

        if tipo == '1':
            matricula = input("Digite sua matrícula: ").strip()
            curso = input("Digite seu curso: ").strip()
            usuario = Aluno(nome, cpf, idade, matricula, curso, senha)
        elif tipo == '2':
            motivo = input("Digite seu motivo para sua visita: ").strip()
            usuario = Visitante(nome, cpf, idade, motivo, senha)
        elif tipo == '3':
            departamento = input("Digite seu departamento: ").strip()
            usuario = ChefeDepartamento(nome, cpf, idade, senha, departamento)
        else:
            raise TipoUsuarioInvalidoError("Tipo de usuário inválido.")

        usuarios.append(usuario)
        print("\nUsuário registrado com sucesso.")
    except UsuarioJaCadastradoError as e:
        print(e)
    except TipoUsuarioInvalidoError as e:
        print(e)
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("Processo de registro finalizado.")

def feedback2():
    print("\nRegistrar informações\n")
    try:
        nota = float(input("Digite a nota (0-10): ").strip())
        if not (0 <= nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        feedback = input("Redija sua crítica: ").strip()
        return nota, feedback
    except ValueError as e:
        print(e)
        return feedback2()

def fazer_feedback(usuario_logado):
    try:
        tipo = input("Tipo de review:\n\n1 - Lugar\n2 - Departamento\nEscolha o seu tipo de feedback: ").strip()

        if tipo == '1':
            local = input("Digite o local: ").strip()
            nota, feedback = feedback2()
            review = FeedbackLocal(nota, feedback, local, usuario_logado)
        elif tipo == '2':
            departamento = input("Digite o departamento: ").strip()
            nota, feedback = feedback2()
            review = FeedbackDepartamento(nota, feedback, departamento, usuario_logado)
        else:
            raise TipoUsuarioInvalidoError("Tipo de review inválido.")

        reviews.append(review)
        print("\nFeedback registrado com sucesso.")
    except TipoUsuarioInvalidoError as e:
        print(e)
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("Processo de feedback finalizado.")

def fazer_login():
    try:
        print("\nFazer login \n")
        cpf = input("\nDigite seu CPF: ").strip()
        senha = input("Digite sua senha: ").strip()

        for usuario in usuarios:
            if usuario.cpf == cpf and usuario.senha == senha:
                print(f"\nBem-vindo, {usuario.nome}!\n")
                return usuario

        raise LoginError("CPF ou senha incorretos.")
    except LoginError as e:
        print(e)
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("Processo de login finalizado.")

def menu():
    usuario_logado = None
    while True:
        print("\nSistema de Feedback\n")
        print("1 - Cadastrar")
        print("2 - Fazer login")
        print("3 - Feedback")
        print("4 - Ver feedbacks")
        print("5 - Sair")
        opcao = input("\nEscolha uma opção: ").strip()

        try:
            if opcao == '1':
                registrar_usuario()
            elif opcao == '2':
                usuario_logado = fazer_login()
            elif opcao == '3':
                if usuario_logado:
                    fazer_feedback(usuario_logado)
                else:
                    print("Você precisa estar logado para fazer um feedback.")
            elif opcao == '4':
                for review in reviews:
                    print(review)
            elif opcao == '5':
                print("\nSaindo...")
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"Erro inesperado no menu: {e}")
        finally:
            print("\nOperação concluída.")

menu()
