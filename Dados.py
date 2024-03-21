def cadastrar_dados():
    nome= input("Digite o nome: ")
    endereço = input("Digite o endereço")
    with open("dados.txt", "a")as arquivos:
        arquivos.write(f"{nome};{endereço}\n")
        print("Dados cadastrados com sucesso!")
        
        def ler_dados():
            try:
                with open("dados.txt","r") as arquivo:
                    print("Lista de dados cadastrados:")
                    for linha in arquivo:
                        dados = linha.strip().split(';')
                        if len(dados) == 2:
                            nome, endereço = dados
                            print(f"Nome: {nome}, Endereço: {endereço}")
                        else:
                            print("Erro ao ler linha do arquivo", linha)
            except FileNotFoundError:
                print("Nenhum cadastro ainda")
                
                def main():
                    while True:
                        print("\n==== Menu de opções ====")
                        print("1. Cadastrar dados")
                        print("Ler dados cadastrados")
                        print("3. Sair")
                        
                        opção = input("Escolha uma opção")
                        
                        if opção == "1":
                            cadastrar_dados()
                        elif opção == "2":
                            ler_dados()
                        elif opção == "1":
                            print("Saindo...")
                            break
                        else :
                            print("Opções inválida. Por favor, escolha uma opção válida")
                        
                        if __name__ == "__main__":
                            main()
                        
                    
                        
