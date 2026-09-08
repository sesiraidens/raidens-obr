"""
Modulo principal do robo OBR (Open Bot Robot).

Contem a classe principal que integra todos os componentes
para a competicao OBR.
"""
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RoboOBR:
    """
    Classe principal do robo OBR.
    
    Integra sensores, motores e logica para a competicao.
    """
    
    def __init__(self):
        self.motores = None
        self.sensores_linha = None
        self.distancia = None
        self.servo = None
        
        self.velocidade_base = 150
        self.velocidade_resgate = 200
        
        self.tempo_inicio = 0
        self.tempo_limite = 120  # 2 minutos
        
        self.estado = "PARADO"
        self.missao_atual = None
        
    def inicializar(self):
        """Inicializa todos os componentes."""
        print("Inicializando robo OBR...")
        
        from src.motores import DriverL298N, ServoMotor
        from src.sensores import MatrizIR, Ultrassonico
        
        self.motores = DriverL298N()
        self.sensores_linha = MatrizIR()
        self.distancia = Ultrassonico()
        self.servo = ServoMotor()
        
        self.servo.centro()
        time.sleep(0.5)
        
        self.estado = "PRONTO"
        print("Robo inicializado.")
        
    def executar_missao(self, nome_missao):
        """
        Executa uma missao especifica.
        
        Args:
            nome_missao: Nome da missao
        """
        self.missao_atual = nome_missao
        self.tempo_inicio = time.time()
        
        print(f"\n{'='*50}")
        print(f"MISSAO: {nome_missao.upper()}")
        print(f"{'='*50}\n")
        
        if nome_missao == "seguir_linha":
            self._missao_seguir_linha()
        elif nome_missao == "resgate":
            self._missao_resgate()
        elif nome_missao == "pista":
            self._missao_pista_completa()
        else:
            print(f"Missao desconhecida: {nome_missao}")
            
    def _missao_seguir_linha(self):
        """Missao: seguir linha preta."""
        self.estado = "SEGUINDO"
        
        while self._tempo_restante() > 0:
            posicao = self.sensores_linha.calcular_posicao()
            
            if not self.sensores_linha.linha_detectada():
                print("Linha perdida! Buscando...")
                self._buscar_linha()
                continue
                
            erro = posicao
            
            vel_esq = self.velocidade_base + erro * 50
            vel_dir = self.velocidade_base - erro * 50
            
            self.motores.mover(int(vel_esq), int(vel_dir))
            
            time.sleep(0.01)
            
        self.motores.parar()
        self.estado = "PARADO"
        
    def _missao_resgate(self):
        """Missao: resgate de vitima."""
        self.estado = "RESCGATE"
        
        self.servo.esquerda()
        time.sleep(0.5)
        
        dist_esq = self.distancia.medir_cm()
        
        self.servo.direita()
        time.sleep(0.5)
        
        dist_dir = self.distancia.medir_cm()
        
        self.servo.centro()
        
        if dist_esq < 30 or dist_dir < 30:
            print("Vitima detectada!")
            self._ir_ate_vitima()
            self._resgatar_vitima()
        else:
            print("Nenhuma vitima encontrada.")
            
        self.motores.parar()
        self.estado = "PARADO"
        
    def _missao_pista_completa(self):
        """Missao: completar pista inteira."""
        self.estado = "PISTA"
        
        etapas = [
            ("Seguir linha", self._missao_seguir_linha),
            ("Intersecao", self._tratar_intersecao),
            ("Resgate", self._missao_resgate)
        ]
        
        for nome, funcao in etapas:
            if self._tempo_restante() > 10:
                print(f"\nEtapa: {nome}")
                funcao()
                
        self.motores.parar()
        self.estado = "FINALIZADO"
        
    def _buscar_linha(self):
        """Busca linha quando perdida."""
        self.motores.esquerda(100)
        time.sleep(0.5)
        
        if self.sensores_linha.linha_detectada():
            return
            
        self.motores.direita(100)
        time.sleep(1.0)
        
        if self.sensores_linha.linha_detectada():
            return
            
        self.motores.frente(100)
        time.sleep(0.5)
        
    def _tratar_intersecao(self):
        """Trata intersecao de linhas."""
        print("Intersecao detectada!")
        
        self.servo.esquerda()
        time.sleep(0.3)
        dist_esq = self.distancia.medir_cm()
        
        self.servo.direita()
        time.sleep(0.3)
        dist_dir = self.distancia.medir_cm()
        
        self.servo.centro()
        
        if dist_esq < 50:
            print("Virando esquerda")
            self.motores.esquerda(150)
            time.sleep(0.5)
        elif dist_dir < 50:
            print("Virando direita")
            self.motores.direita(150)
            time.sleep(0.5)
        else:
            print("Seguindo reto")
            
    def _ir_ate_vitima(self):
        """Move ate a vitima."""
        self.motores.frente(self.velocidade_resgate)
        
        while self.distancia.medir_cm() > 15:
            time.sleep(0.1)
            
        self.motores.parar()
        
    def _resgatar_vitima(self):
        """Executa acao de resgate."""
        print("Resgatando vitima!")
        
        self.servo.mover(45)
        time.sleep(0.5)
        
        self.motores.tras(200)
        time.sleep(1)
        
        self.motores.parar()
        
    def _tempo_restante(self):
        """Calcula tempo restante."""
        elapsed = time.time() - self.tempo_inicio
        return max(0, self.tempo_limite - elapsed)
        
    def status(self):
        """Retorna status atual."""
        return {
            "estado": self.estado,
            "missao": self.missao_atual,
            "tempo_restante": self._tempo_restante(),
            "linha": self.sensores_linha.ler_todos() if self.sensores_linha else None,
            "distancia": self.distancia.medir_cm() if self.distancia else None
        }
        
    def parar(self):
        """Para o robo."""
        self.motores.parar()
        self.estado = "PARADO"
        print("Robo parado.")
