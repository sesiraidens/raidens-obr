<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" width="80">

# raidens-obr

Software completo para robo OBR (Open Bot Robot) da competicao MNR.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=flat&logo=arduino&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-d9333b?style=flat)
![Status](https://img.shields.io/badge/Status-Active-2ea043?style=flat)

</div>

---

## Sobre

O **raidens-obr** contem o software completo para o robo da competicao MNR/RoboCup. Inclui navegacao por linha, resgate de vitimas e gerenciamento de tempo.

---

## Estrutura

`
raidens-obr/
├── src/
│   ├── robo_obr.py       # Classe principal
│   └── __init__.py
├── examples/
│   ├── executar_missao.py
│   └── teste_sensores.py
└── README.md
`

---

## Missoes

### Seguir Linha

O robo segue linha preta usando PID com 5 sensores IR.

`python
robo.executar_missao("seguir_linha")
`

**Comportamento:**
- Detecta linha com MatrizIR
- Calcula posicao (-2 a +2)
- Ajusta motores via PID
- Busca linha quando perdida

### Resgate

O robo detecta e resgata vitimas.

`python
robo.executar_missao("resgate")
`

**Comportamento:**
- Escaneia area com servo
- Detecta obstaculos com ultrassonico
- Move ate vitima
- Executa acao de resgate

### Pista Completa

Executa todas as missoes em sequencia.

`python
robo.executar_missao("pista")
`

**Etapas:**
1. Seguir linha
2. Tratar intersecoes
3. Resgate de vitimas

---

## Uso

### Inicializar

`python
from src.robo_obr import RoboOBR

robo = RoboOBR()
robo.inicializar()
`

### Executar Missao

`python
robo.executar_missao("seguir_linha")
`

### Verificar Status

`python
status = robo.status()
print(f"Estado: {status['estado']}")
print(f"Tempo: {status['tempo_restante']:.0f}s")
`

### Parar

`python
robo.parar()
`

---

## Configuracao

### Parametros Principais

| Parametro | Padrao | Descricao |
|---|---|---|
| elocidade_base | 150 | Velocidade de seguimento |
| elocidade_resgate | 200 | Velocidade de resgate |
| 	empo_limite | 120s | Tempo maximo de missao |

### Ajustar Velocidade

`python
robo.velocidade_base = 180
robo.velocidade_resgate = 220
`

---

## Hardware

| Componente | Pino | Descricao |
|---|---|---|
| Motor Esq ENA | 5 | PWM motor esquerdo |
| Motor Dir ENB | 6 | PWM motor direito |
| IR 1-5 | A0-A4 | Sensores de linha |
| Trigger | 9 | Ultrassonico trigger |
| Echo | 10 | Ultrassonico echo |
| Servo | 11 | Servo de varredura |

---

## Equipe

**RAIDENS - SESI Aluminio 192**

Desenvolvido para uso interno da equipe. Licenciado sob MIT.