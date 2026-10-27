<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="140">

# raidens-obr

**Software do robô da RAIDENS para a Olimpíada Brasileira de Robótica**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-IDE-00979D?style=flat-square&logo=arduino&logoColor=white)
![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-D9333B?style=flat-square)

[Sobre](#sobre) · [Instalação](#instalação) · [Missões](#missões) · [Uso](#uso) · [Hardware](#hardware) · [Documentação](#documentação)

</div>

---

## Sobre

O **raidens-obr** é onde as bibliotecas da equipe viram um robô de competição. A classe `RoboOBR` junta sensores, motores e cronômetro e organiza a prova da [OBR](https://obr.robocup.org.br/) em missões: seguir a linha, resgatar vítimas e cumprir a pista completa dentro do tempo limite.

Cada missão é um método separado. Assim dá para treinar e depurar uma etapa da prova sem rodar todas as outras.

## Instalação

```bash
git clone https://github.com/sesiraidens/raidens-obr.git
cd raidens-obr
```

O `RoboOBR` importa `src.motores` e `src.sensores`. Copie para a pasta `src/` os arquivos `motores.py` do [`raidens-motores`](https://github.com/sesiraidens/raidens-motores) e `sensores.py` do [`raidens-sensores`](https://github.com/sesiraidens/raidens-sensores) antes de executar.

## Missões

| Missão | Chave | Comportamento |
|---|---|---|
| **Seguir linha** | `seguir_linha` | Lê a matriz de 5 sensores IR, calcula a posição da linha (−2 a +2), corrige os motores e procura a linha quando ela se perde |
| **Resgate** | `resgate` | Varre a área com o servo, detecta a vítima com o ultrassônico, vai até ela e executa o resgate |
| **Pista completa** | `pista` | Encadeia seguir linha, tratamento de interseções e resgate |

## Uso

```python
from src.robo_obr import RoboOBR

robo = RoboOBR()
robo.inicializar()

robo.executar_missao("seguir_linha")

status = robo.status()
print(f"Estado: {status['estado']} · Tempo restante: {status['tempo_restante']:.0f}s")

robo.parar()
```

### Parâmetros

| Atributo | Padrão | Descrição |
|---|---|---|
| `velocidade_base` | 150 | PWM ao seguir linha |
| `velocidade_resgate` | 200 | PWM na área de resgate |
| `tempo_limite` | 120 s | Tempo máximo da prova |

```python
robo.velocidade_base = 180
robo.velocidade_resgate = 220
```

## Hardware

| Componente | Pino | Função |
|---|---|---|
| Motor esquerdo (ENA) | 5 | PWM |
| Motor direito (ENB) | 6 | PWM |
| IR 1 a 5 | A0 a A4 | Sensores de linha |
| Ultrassônico trigger | 9 | Disparo |
| Ultrassônico echo | 10 | Retorno |
| Servo | 11 | Varredura do resgate |

## Documentação

| Documento | Para quê |
|---|---|
| [`docs/checklist-submissao.md`](docs/checklist-submissao.md) | Conferir tudo antes de enviar a inscrição |
| [`docs/links-uteis.md`](docs/links-uteis.md) | Site, regulamento e categorias da OBR |
| [`templates/README.md`](templates/README.md) | Modelo de README para novos projetos da equipe |

## Estrutura

```text
raidens-obr/
├── src/          # RoboOBR e as missões
├── docs/         # Material de apoio para a competição
└── templates/    # Modelos para novos projetos
```

## Ecossistema RAIDENS

Este repositório faz parte de um conjunto de bibliotecas da equipe. Elas usam os mesmos nomes de classes e convenções, então o que você aprende em uma serve nas outras.

| Repositório | Para quê |
|---|---|
| [`raidens-python`](https://github.com/sesiraidens/raidens-python) | Biblioteca principal em Python: sensores, motores e robôs prontos (seguidor, parede, resgate) |
| [`raidens-arduino`](https://github.com/sesiraidens/raidens-arduino) | As mesmas abstrações em C++ para rodar direto no Arduino |
| [`raidens-sensores`](https://github.com/sesiraidens/raidens-sensores) | Catálogo completo de sensores com calibração e filtragem |
| [`raidens-motores`](https://github.com/sesiraidens/raidens-motores) | Motores DC, servo, passo, driver L298N e rodas mecanum |
| [`raidens-pid`](https://github.com/sesiraidens/raidens-pid) | Controladores PID, PID avançado, cascata e sintonia Ziegler-Nichols |
| [`raidens-opencv`](https://github.com/sesiraidens/raidens-opencv) | Visão computacional: cores, linhas e navegação por câmera |
| [`raidens-lab`](https://github.com/sesiraidens/raidens-lab) | Calibração interativa de cores em HSV e LAB |
| [`raidens-electronics`](https://github.com/sesiraidens/raidens-electronics) | Cálculos e modelos de componentes eletrônicos |
| [`raidens-3d`](https://github.com/sesiraidens/raidens-3d) | Peças 3D paramétricas geradas em OpenSCAD |
| [`raidens-ros`](https://github.com/sesiraidens/raidens-ros) | Estrutura de nodes e tópicos ROS 2 |
| [`raidens-snippets`](https://github.com/sesiraidens/raidens-snippets) | Trechos de código prontos para copiar e colar |

---

<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="56">

**Equipe RAIDENS** · SESI 192 Alumínio/SP

[![Email](https://img.shields.io/badge/Email-sesiraidens%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sesiraidens@gmail.com)
[![Linktree](https://img.shields.io/badge/Linktree-sesiraidens-39E06B?style=flat-square&logo=linktree&logoColor=white)](https://linktr.ee/sesiraidens)
[![GitHub](https://img.shields.io/badge/GitHub-sesiraidens-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sesiraidens)

<sub>Desenvolvido pela equipe RAIDENS para fins educacionais. Licenciado sob MIT.</sub>

</div>







