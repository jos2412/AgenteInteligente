MOVIMIENTOS = {
            'primero' : 'Tira cuadro 5',
            'segundo' : 'espera turno',
            'cuadro 7' : 'Tira cuadro 8',  
            'cuadro 2' : 'Tira cuadro 4', 
            'cuadro 6' : 'Tira cuadro 1',
            'cuadro 9' : 'Tira cuadro 3',
            
            'cuadro 8' : 'Tira cuadro 7',  
            'cuadro 4' : 'Tira cuadro 2', 
            'cuadro 1' : 'Tira cuadro 6',
            'cuadro 3' : 'Tira cuadro 9',            
           
            }
# %%

class AgenteInteligente:
    """Agente racional de tipo tabla"""

    def __init__(self, movimientos):
        self.movimientos = movimientos
        

    def actuar(self, percepcion, accion_basica=''):
        """Actua segun la percepcion, devolviendo una accion."""
        if not percepcion:
            return accion_basica       
        if percepcion in self.movimientos.keys():  
            return self.movimientos[percepcion] 
            
        return accion_basica
# %%
        

        print("TIC TAC TOE --")
        agente = AgenteInteligente(MOVIMIENTOS)
        percepcion = input("MOVIMIENTO  INICIAL: ")
        while percepcion: 
            accion = agente.actuar(percepcion, 'reiniciarse')
            print(accion)
            percepcion = input("MOVIMIENTO OPONENTE:")



