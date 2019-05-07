import time



class Grafo():
    def __init__(self,palabra):
        pass
    def run(self):
        pass
    def buscarTransicion(self,a,b):
        pass
    def modificarPila(self,meter):
        pass
    def imprimirEstado(self):
        pass






class Automata(Grafo):
    def __init__(self,palabra):
        self.__indexP=0
        self.__indexE=0
        self.__palabra=list(palabra)
        self.__palabra.append("λ")
        self.__pila=Pila()
        self.__vertices=[Vertice([Transicion("b","b","bb",1),Transicion("a","b","ba",2),Transicion("b","a","ab",3),Transicion("a","a","aa",4),Transicion("b","#","#b",5),Transicion("a","#","#a",6),Transicion("c","#","#",7),Transicion("c","b","b",8),Transicion("c","a","a",9)]),Vertice([Transicion("b","b","λ",1),Transicion("a","a","λ",2),Transicion("λ","#","#",3)]),Vertice([None])]
        self.__desapilado="0"
        self.__trancisionActual=0
        self.__vandera=False
        self.__isEjecucion=False
        self.__isPalimdrome=False

    def getVandera(self):
        return self.__vandera
    def setVandera(self,sw):
        self.__vandera=sw
    def getTransicion(self):
        return self.__trancisionActual
    def getLetra(self):
        return self.__indexP
    def getEstado(self):
        return self.__indexE
    def getPila(self):
        return self.__pila
    def isRunAutomata(self):
        return self.__isEjecucion
        
    def isPalimdrome(self):
        return self.__isPalimdrome
    
    def run(self):
        self.__isEjecucion=True
        sw=True
        while self.__indexP < (len(self.__palabra)) and self.__indexE != 2 and sw!=False: 
            self.esperarVandera()
            if self.__indexE != 2:
                l=self.__palabra[self.__indexP]
                lp=self.__pila.getTope()
                transicion=self.buscarTransicion(l,lp)
                if self.operar(transicion,l)==0:
                    sw=False
                    print (self.__indexE)
                self.__indexP+=1
            else:
                print( "palimdrome")
                break
            
    
            if( self.__indexE == 2):
                print(" es palindromo")
                self.__isEjecucion=False
                self.__isPalimdrome=True
                break
            if( sw!=True):
                self.__isEjecucion=False
                print("no es palindrome")
                break

            self.__vandera=False
            print("----------------------------------------------------------------")
        print("AUTOMATA DETENIDO ")
        
    def esperarVandera(self):
        while(self.__vandera==False):

            time.sleep(0.2)
            if(self.__vandera==True):
                break
    def buscarTransicion(self,a,b):
        index=self.__vertices[self.__indexE].buscarTrans(a,b)
        if index!= -1:
            self.__trancisionActual=self.__vertices[self.__indexE].transicionesTH[index].getTrans()
            return self.__vertices[self.__indexE].transicionesTH[index].getl3()
        else:
            return None

    def operar(self,expresion,l):
        if expresion!=None:
            if l=="c" or l=="λ" :
                self.modificarPila(expresion)
                self.__indexE+=1
            else:    
                self.modificarPila(expresion)
            return 1
        else:
            print("No palimdrome")
            return 0
    
    def modificarPila(self,meter):
        self.__desapilado=self.__pila.desapilar()
        j=0
        for i in meter:
            self.__pila.apilar(meter[j])
            j+=1
    def imprimirEstado(self):
        j=0
        print("pila = ",self.__pila.vec)
        for target_list in self.__pila.vec:
            print(j," ",self.__pila.vec[j])
            j+=1
        print("estado = ",self.__indexE)
        print("letra = ",self.__indexP)
        print("desapilado ",self.__desapilado)
        