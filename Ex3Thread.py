import multiprocessing
import time
import random

def sapo(id,dm):
    dp=0
    tmp = 5
    print(f"Sapo {id} largou!")
    while dp < dm:
        pulo = random.randint(1,tmp)
        dp += pulo
        print(f"Sapo {id} deu um salto de {pulo} cm ")
        print(f"Distancia percorrida: {dp} cm | Distancia maxima: {dm} cm")
        time.sleep(0.2)
    print(f"O sapo {id} cruzou a linha de chegada!")

def main():
    dm=20
    sapo1,sapo2,sapo3,sapo4,sapo5=1,2,3,4,5
    print("Iniciando corrida de sapos!")
    with multiprocessing.Pool(processes=5) as pool:
        pool.starmap(sapo, [(sapo1,dm),(sapo2,dm),(sapo3,dm),(sapo4,dm),(sapo5,dm)])

    print("Corrida finalizada!")

if __name__ == "__main__":
    main()
    
