import threading as th
import os 

Name = input("Enter the name to scrape: ")

def threads_execution():
    os.system(f"echo {Name} | python threads.py ")               # Add the file path properly to make it work 

def x_execution():
    os.system(f"echo {Name} | python x.py ")                     # Add the file path properly to make it work 


def linkedin_execution():
   os.system(f"echo {Name} | python Linkedin.py ")               # Add the file path properly to make it work 


def Instagram_execution():
    os.system(f"echo {Name} | python instagram.py ")             # Add the file path properly to make it work 



t1 = th.Thread(target=threads_execution,daemon=True)
t2 = th.Thread(target=x_execution, daemon=True)
t3 = th.Thread(target=linkedin_execution, daemon=True)
t4 = th.Thread(target=Instagram_execution,daemon=True)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

