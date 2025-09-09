# Jokenpô

Um minigame de jokenpô em Python que roda no terminal, com três níveis de dificuldade. No nível mais alto, vencer é matematicamente impossível.

Este projeto foi desenvolvido para uma disciplina da faculdade. Durante a apresentação, muitos colegas ficaram confusos com a mecânica das dificuldades, principalmente pela abordagem do modo difícil, no qual a vitória é inviável por construção.

Decidi disponibilizar este jogo aqui para que vocês possam entender a lógica por trás dele e, quem sabe, adaptá-la ou aplicá-la em outros contextos.

A “virada de chave” está presente na linha 30, onde existe um pequeno cálculo:
jogada_maquina_m3 = (jogada_user_m3 + 1) % 3


À primeira vista, essa linha pode parecer confusa, mas é bastante precisa e inteligente. As escolhas Pedra, Papel e Tesoura são representadas por 0, 1 e 2, respectivamente.

Por exemplo, se o usuário jogar Tesoura (2):

jogada_maquina_m3 = (2 + 1) % 3  
jogada_maquina_m3 = 0  # Pedra


E o que acontece? A máquina sempre escolhe a jogada seguinte, ou seja, a que vence a do jogador.

Segue a tabela para visualizar melhor:

<img width="451" height="269" alt="image" src="https://github.com/user-attachments/assets/62ef92ee-2f38-4c03-80d6-165bf7e5acf9" />
