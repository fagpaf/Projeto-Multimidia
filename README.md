# 🐤 Flappy Bird (Pygame)

Um remake do clássico **Flappy Bird**, desenvolvido em **Python com Pygame**.  
O objetivo é simples: pressione **ESPAÇO** para fazer o pássaro voar e evitar os canos!

---

## 🧩 Estrutura do Projeto


    ├── main.py
    ├── Game.py
    ├── Bird.py
    ├── Pipe.py
    │
    ├── assets/
    │   ├── audio/                  
    │   │   ├── Theme For FlappyBird.wav
    │   │   ├── hit.wav
    │   │   ├── point.wav
    │   │   └── wing.wav
    │   │
    │   ├── sprites/                
    │   │   ├── flappy-bird-background-800x600.png
    │   │   ├── pipe-green.png
    │   │   ├── yellowbird-midflap.png
    │   │   ├── bluebird-midflap.png
    │   │   └── redbird-midflap.png
    │   │
    │   └── demo/
    │       └── demo.mp4
    ├── favicon.ico
    │
    ├── README.md
    └── LICENSE



---

## ⚙️ Requisitos

- **Python 3.10+**
- **Pygame**

---

## Instale as dependências:
    pip install pygame

## 🎮 Controles

```
ESPAÇO → Faz o pássaro pular
Fechar janela → Sai do jogo
```

## 🎵 Recursos de Áudio
| Som | Arquivo                    | Ação                   |
| --- | -------------------------- | ---------------------- |
| 🎶  | `Theme For FlappyBird.wav` | Música de fundo (loop) |
| 🕊  | `wing.wav`                 | Pulo                   |
| 💥  | `hit.wav`                  | Colisão                |
| 🏅  | `point.wav`                | Pontuação              |

## Jogando
<video src="assets/demo/gameplay.mp4" width="500" autoplay loop muted></video>