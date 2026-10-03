# variaveis para registrar que aquele processo ja foi feito
cadastro_salvo = False
avaliacao_salvo = False
agendamento_salvo = False

# variaveis globais para salvar as informacoes
# funcionalidade 1
nome = ""
cpf = ""
email = ""
telefone = ""

# funcionalidade 2
prioridade = ""

# funcionalidade 3
local = ""
local_atendimento = ""
dias_espera = 0

# separamos as funcionalidades em funcoes para organizacao e pra poder usar na verificacao de sobrescrever no loop principal

# definimos a funcao do cadastro
def realizar_cadastro():
    global cadastro_salvo, nome, cpf, email, telefone # a gente declara essas variaveis como Globais pra poder escrever
                                                      # diretamente nas variaveis globais do codigo e não numa variavel local dentro da funcao

    print("\nCADASTRO:")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")

    tem_email = False
    tem_telefone = False

    #usamos um loop para forcar o usuario a repetir o processo caso nao tenha incluido nemhum email nem telefone
    while not tem_email and not tem_telefone:

        #perguntamos ao usuario se ele quer cadastrar o email, dentro de um loop basico pra garantir que ele responda sim ou nao
        cadastrar_email = ""
        while cadastrar_email != 's' and cadastrar_email != 'n':
            cadastrar_email = input("Você quer adicionar um email? (s/n): ").lower()


        if cadastrar_email == "s":     #se ele quer cadastrar o email entao salva o email com o input dele
            email = input("Digite seu email: ")
            tem_email = True

        cadastrar_telefone = ""
        while cadastrar_telefone  != 's' and cadastrar_telefone != 'n':
            cadastrar_telefone = input("Você quer adicionar um telefone? (s/n): ").lower()

        if cadastrar_telefone == "s":
            telefone = input("Digite seu telefone: ")
            tem_telefone = True

        if not tem_email and not tem_telefone:   #se ele nao tiver informado nenhum meio de contato, é avisado e o loop repete
            print("\nADICIONE PELO MENOS UM EMAIL OU TELEFONE\n")
        else:   #se tem pelo menos um telefone ou email ele vai registrar que salvou
            cadastro_salvo = True
            print("\nCadastro salvo\n")


# definimos a funcao da avaliacao
def realizar_avaliacao():
    global avaliacao_salvo, prioridade

    print("\nAVALIAÇÃO")

    #primeiro coletamos os dados para a avaliacao
    dias_sem_atendimento = int(input("Há quantos dias necessita de atendimento? "))
    nivel_dor = int(input("Qual o nível de dor? (0-10): "))

    pontuacao_total = dias_sem_atendimento + (nivel_dor * 2) #calculamos a pontuacao baseado no dias e o nivel de dor com peso maior

    print(f"\nSua pontuação baseada nos sintomas é: {pontuacao_total}")

    #baseado na pontuacao, categorizamos o nivel de prioridade em 3 categorias
    if pontuacao_total <= 8:
        prioridade = "risco baixo"
    elif pontuacao_total <= 15:
        prioridade = "risco controlado"
    else:
        prioridade = "risco urgente"

    print(f"Prioridade = {prioridade}")
    avaliacao_salvo = True

# definimos a funcao de agendamento
def realizar_agendamento():
    global agendamento_salvo, local, local_atendimento, dias_espera

    #verificamos se o usuario ja realizou o cadastro e a avaliacao, é necessario possuir os dois para prosseguir com o encaminhamento
    if cadastro_salvo == False:
        print("\nRegistre um cadastro primeiro.\n")
    elif prioridade == "":
        print("\nVocê precisa realizar uma avaliação antes de agendar\n")
    else:

        print("\nENCAMINHAMENTO / AGENDAMENTO")

        # cada nivel de prioridade tem uma quantidade de dias de espera definida
        if prioridade == "risco urgente":
            dias_espera = 1
        elif prioridade == "risco controlado":
            dias_espera = 3
        else:
            dias_espera = 7

        print(f"Com base na sua avaliação ({prioridade}), temos uma visita disponível em {dias_espera} dia(s).")

        confirmar = input("Deseja agendar? (s/n): ").lower()


        # caso o usuario queira agendar, é feita uma verificacao de localizacao do usuario
        if confirmar == 's':

            print("\nSelecione o bairro em que você reside ou o mais próximo:")
            print("1 - Lapa")
            print("2 - Pinheiros")
            print("3 - Sé")
            print("4 - República")
            print("5 - Mooca")
            print("6 - Tatuapé")


            # criamso um loop basico para forcar o usuario a escolher um bairro existente nas opcoes

            bairro = 0
            local_atendimento = ""

            while bairro < 1 or bairro > 6:

                bairro = int(input("Digite o número correspondente ao seu bairro (1-6): "))

                # cada local de atendimento atende a 2 bairros, entao se o usuario escolher uma das duas opcoes de bairros
                # daquele local de atendimento, aquele local vai ser escolhido

                if bairro == 1 or bairro == 2:
                    local_atendimento = "Local A (Clínica Zona Oeste)"
                elif bairro == 3 or bairro == 4:
                    local_atendimento = "Local B (Clínica Centro)"
                elif bairro == 5 or bairro == 6:
                    local_atendimento = "Local C (Clínica Zona Leste)"
                else:
                    print("\nOpção de bairro inválida.")


            # imprimimos o resumo com todos os dados importantes do agendamento

            print("===================================================")
            print("RESUMO DO AGENDAMENTO")

            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")

            # checa se existe a informacao do email e do telefone para imprimir
            if email != "":
                print(f"Email: {email}")
            if telefone != "":
                print(f"Telefone: {telefone}")

            print(f"Status: {prioridade.upper()}")
            print(f"Local: {local_atendimento}")
            print(f"Data: Visitar o local em {dias_espera} dia(s).")
            print("===================================================")

            agendamento_salvo = True

        else:
            print("\nAgendamento cancelado. Retornando ao menu...\n")



# aqui é o loop principal onde vai ter a lógica do programa e menu

print("Bem vindo ao programa Apolônias do Bem!")
print("---------------------------------------")

while True:
    print("===================================================")
    print("MENU:")
    print("1 - CADASTRO")
    print("2 - AVALIAÇÃO")
    print("3 - AGENDAMENTO")
    print("4 - ENCERRAR")
    print("===================================================")

    escolha = int(input("\nDigite sua escolha: "))

    # apos apresentar as opcoes e o usuario escolher, vai para cada escolha
    # todas as escolhas checam se o usuario ja possui dados salvos, dando a escolha
    # de sobrescrever aqueles dados, ou retornar ao menu novamente

    if escolha == 1:  # se for a primeira escolha

        if cadastro_salvo == True:  # verifica se ja existe um cadastro

            # loop para garantir que o usuario responda sim ou nao
            sobrescrever = ""
            while sobrescrever !="s" and sobrescrever != "n":
                sobrescrever = input("Você já tem um cadastro salvo, deseja sobrescrever? (s/n)")

                    #se o usuario quiser sobrescrever entao chama a funcao realizar_cadastro() definida antes
                if sobrescrever == "s":
                   realizar_cadastro()
                elif sobrescrever == "n":
                    break   # se ele nao quiser ai interrompe esse loop
                else:
                    print("Opção inválida. Por favor, digite 's' para sim e 'n' para não")  #so um aviso que a opcao eh invalida antes de perguntar de novo

        else:   #se nao tiver cadastro salvo chama direto a funcao do cadastro
            realizar_cadastro()

        #a escolha 2 segue a mesma estrutura e logica da escolha 1, mas chamando a funcao realizar_avaliacao()
    elif escolha == 2:

        if avaliacao_salvo == True:

            sobrescrever = ""
            while sobrescrever != "s" and sobrescrever != "n":
                sobrescrever = input("Deseja refazer a avaliação? (s/n)")

                if sobrescrever == "s":
                    realizar_avaliacao()
                elif sobrescrever == "n":
                    break
                else:
                    print("Opção inválida. Por favor, digite 's' para sim e 'n' para não")

        else:
            realizar_avaliacao()

        #a escolha 3 tambem segue a mesma logica, so muda que se tiver um agendamento ele repassa o resumo do agendamento antes de perguntar para sobrescrever
    elif escolha == 3:

        if agendamento_salvo == True:

            print ("\nVocê já possui um agendamento:\n")

            print("===================================================")
            print("RESUMO DO AGENDAMENTO")

            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")

            if email != "":
                print(f"Email: {email}")
            if telefone != "":
                print(f"Telefone: {telefone}")

            print(f"Status: {prioridade.upper()}")
            print(f"Local: {local_atendimento}")
            print(f"Data: Visitar o local em {dias_espera} dia(s).")
            print("===================================================")

            sobrescrever = ""
            while sobrescrever != "s" and sobrescrever != "n":
                sobrescrever = input("\nVocê já tem um agendamento, deseja sobrescrever? (s/n)")

                if sobrescrever == "s":
                    realizar_agendamento()
                elif sobrescrever == "n":
                    break
                else:
                    print("Opção inválida. Por favor, digite 's' para sim e 'n' para não")

        else:
            realizar_agendamento()

        #a escolha 4 eh a opcao de sair entao simplesmente da um break pra encerrar o loop principal
    elif escolha == 4:
        print("\nEncerrando o programa Apolônias do Bem.")
        break

    else:   # se o usuario nao digitar uma das opcoes do menu, apenas informa ele e o loop vai reiniciar de volta pro menu
        print("\nOpção inválida. Por favor, escolha um número de 1 a 4.")




