def pode_dirigir(idade, possui_carteira, nao_esta_bloqueado):
    return idade >= 18 and possui_carteira and nao_esta_bloqueado


if pode_dirigir(idade, possui_carteira, nao_esta_bloqueado):
    print("Pode dirigir")
else:
    print("Não pode dirigir")