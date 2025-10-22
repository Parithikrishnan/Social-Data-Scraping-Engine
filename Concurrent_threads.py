import threading as th
import os 

Name = input("Enter the name to scrape: ")

def threads_execution():
    os.system(f"echo {Name} | python sites/threads.py ")               # Add the file path properly to make it work 

def x_execution():
    os.system(f"echo {Name} | python sites/x.py ")                     # Add the file path properly to make it work 

def linkedin_execution():
   os.system(f"echo {Name} | python sites/Linkedin.py ")               # Add the file path properly to make it work 

def Instagram_execution():
    os.system(f"echo {Name} | python sites/instagram.py ")             # Add the file path properly to make it work 

def Youtube_execution():
    os.system(f"echo {Name} | python sites/Youtube.py")

def Reddit_execution():
    os.system(f"echo {Name} | python sites/Reddit.py")

def Quora_execution():
    os.system(f"echo {Name} | python sites/Quora.py")

t1 = th.Thread(target=threads_execution,daemon=True)
t2 = th.Thread(target=x_execution, daemon=True)
t3 = th.Thread(target=linkedin_execution, daemon=True)
t4 = th.Thread(target=Instagram_execution,daemon=True)
t5 = th.Thread(target=Youtube_execution,daemon=True)
t6 = th.Thread(target=Reddit_execution,daemon=True)
t7 = th.Thread(target=Quora_execution,daemon=True)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()

