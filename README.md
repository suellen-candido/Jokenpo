# Jokenpô
Um minigame de jokenpô em Python que roda no terminal, com três níveis de dificuldade. No nível mais alto, vencer é matematicamente impossível.

Este projeto foi desenvolvido para uma disciplina da faculdade. Durante a apresentação, muitos colegas ficaram confusos com a mecânica das dificuldades, principalmente pela abordagem do modo difícil, no qual a vitória é inviável por construção.

Decidi disponibilizar este jogo aqui para que vocês possam entender a lógica por trás dele e, quem sabe, adaptá-la ou aplicá-la em outros contextos. Básicamente, a virada de chave está presente na linha 30, onde possui um pequeno cálculo: jogada_maquina_m3 = (jogada_user_m3 + 1) % 3. A principio quando você olha essa linha ela parece bem confusa, entretanto ela é bastante precisa e inteligente, o que acontece é que as escolhas: Pedra, Papel e Tesoura são respectivamente 0, 1 e 2, dito isso, vamos ver como fica a conta se o usuário jogasse Tesoura(2): jogada_maquina_m3 = (2 + 1) % 3 -> jogada_maquina_m3 = 0 (Pedra).

Você percebeu o detalhe? A jogada da máquia sempre vai vencer, pois, a jogada que ganha é a próxima, segue a tabela:

<img width="451" height="269" alt="image" src="https://github.com/user-attachments/assets/62ef92ee-2f38-4c03-80d6-165bf7e5acf9" />
