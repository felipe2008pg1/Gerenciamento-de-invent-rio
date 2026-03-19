listap = []

while True:
    try:
        menu = int(input("\n1-Add | 2-Listar | 3-Remover | 4-Sair: "))
    except ValueError:
        print("Erro: Digite apenas o NÚMERO das opções.")
        continue

    if menu == 1:
        try:
            nome = input("Nome: ").strip()
            qtd = int(input("Qtd: "))
            preco = float(input("Preço: "))

            # VALIDAÇÃO: Só entra na lista se passar aqui
            if qtd <= 0 or preco <= 0:
                print("❌ ERRO: Valores inválidos (devem ser > 0).")
            else:
                item = {"nome": nome, "quantidade": qtd, "preco": preco}
                listap.append(item) # SÓ UM APPEND, e só aqui.
                print(f"✅ {nome} adicionado!")
        except ValueError:
            print("❌ ERRO: Quantidade e Preço devem ser números!")

    elif menu == 2:
        if not listap:
            print("Lista vazia.")
        else:
            for i, p in enumerate(listap):
                print(f"[{i}] {p['nome']} - Qtd: {p['quantidade']} - R$ {p['preco']:.2f}")

    elif menu == 3:
        if not listap:
            print("Nada para remover.")
            continue
        
        try:
            for i, p in enumerate(listap):
                print(f"{i}: {p['nome']}")
            
            escolha = int(input("Índice para remover: "))
            removido = listap.pop(escolha)
            print(f"🗑️ {removido['nome']} removido!")
        except (ValueError, IndexError):
            print("❌ ERRO: Escolha um índice válido (número da lista).")

    elif menu == 4:
        print("Saindo...")
        break
