tam_arquivo = int(input("Quantos megabytes tem o arquivo?: "))
vel_conexao = int(input("Quantos Mbps tem a sua internet?: "))


vel_c =  (vel_conexao / 8) 


tempo = (tam_arquivo / vel_c) / 60 

print(tempo)