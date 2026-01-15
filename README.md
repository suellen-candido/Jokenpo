# Jokenpô em Python

Um **minigame de Jokenpô (Pedra, Papel e Tesoura)** desenvolvido em **Python**, executado no terminal.  
O jogo possui **três níveis de dificuldade**, sendo que, no nível mais alto, **vencer é matematicamente impossível por construção**.

Este projeto foi desenvolvido para uma **disciplina da faculdade**. Durante a apresentação, muitos colegas ficaram confusos com a mecânica das dificuldades — principalmente no **modo difícil**, que foge do comportamento tradicional do jogo.  
Por isso, decidi disponibilizar este repositório para explicar melhor a lógica utilizada e permitir que outras pessoas possam entendê-la, adaptá-la ou aplicá-la em outros contextos.

---

## Níveis de Dificuldade

- **Fácil**: a máquina realiza escolhas simples.
- **Médio**: comportamento mais equilibrado.
- **Difícil**: a máquina **sempre vence o jogador**, tornando a vitória inviável.

O diferencial deste projeto está no **modo difícil**, que utiliza uma lógica matemática simples e eficiente para garantir a vitória da máquina.

---

## Lógica do Modo Difícil

A principal “virada de chave” do algoritmo está na seguinte linha de código:

```python
jogada_maquina_m3 = (jogada_user_m3 + 1) % 3 
```


## Visualização da Lógica

A tabela abaixo mostra como a máquina sempre seleciona a jogada vencedora em relação à escolha do jogador:
<img width="451" height="269" alt="image" src="https://github.com/user-attachments/assets/62ef92ee-2f38-4c03-80d6-165bf7e5acf9" />

