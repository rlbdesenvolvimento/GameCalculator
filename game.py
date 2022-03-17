from models.calcular import Calcular


def main():
    pontos = 0
    jogar(pontos)


def jogar(pontos: int):
    dificuldade: int = int(input('Informe o nível de dificuldade desejado: [1, 2 ,3 ou 4]'))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input("Deseja continuar no jogo? [1 - sim, 0 - não] "))

    if continuar == 1:
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
