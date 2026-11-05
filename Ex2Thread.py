import multiprocessing
import time     
import random

def soma(id,vtr):
    soma=0
    for i in vtr:
        soma +=i
        time.sleep(0.5)
    print(f"Thread #{id} - Soma: {soma}")

    

def main():
    parametros=[0]*3
    for i in range(3):
        id = i+1
        vl1 = random.randint(1,100)
        vl2 = random.randint(1,100)
        vl3 = random.randint(1,100)
        vl4 = random.randint(1,100)
        vl5 = random.randint(1,100)

        vtr = [vl1,vl2,vl3,vl4,vl5]
        parametros[i] = (id,vtr)
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(soma, parametros)



       

if __name__ == "__main__":
    main()
    
