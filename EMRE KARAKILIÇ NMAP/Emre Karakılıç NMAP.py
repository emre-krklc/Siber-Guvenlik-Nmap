import os
import subprocess

def mainMenu():
    print("-"*80)
    print("\t\t\t NMAP SECURITY SCANNER")
    print("-"*80)
    print()
    print("\t\t\t1---> Host Discovery")
    print("\t\t\t2---> OS Discovery")
    print("\t\t\t3---> Port Discovery")
    print("\t\t\t4---> Port Bulma Aralığı")
    print("\t\t\t5---> Ekranı Temizle")
    print("\t\t\t6---> Programı Kapat")
    print()
    choice = int(input("Seçeneklerden Bir Tanesini Seçin"))
    if choice == 1:
        Host_DisCov()
        mainMenu()
    elif choice == 2:
        os_discovery()
        mainMenu()
    elif choice == 3:
        port_discovery()
        mainMenu()
    elif choice == 4:
        port_discoveryInRange()
        mainMenu()
    elif choice == 5:
         clear()
         mainMenu()
    elif choice == 6:
        clear()
        quit_Program()
    else:
        print("Invalid Choice :(")
        mainMenu()





 



def Host_DisCov():
    host=input("[*]Lutfen Taranacak Ana Bilgisayar Adresini Girin : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-v', '-Pn', '-sn','-sL','-PE', '-PP','-oN','hostlist.txt', host])
    print('-' * 80)



def os_discovery():
    os = input("[*]Lutfen Taranacak Ana Bilgisayar Adresini Girin : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-F','-A','-v', '-Pn','-sS','-O','-oN','os_Discove.txt', os])
    print('-' * 80)



def port_discovery():
    port = input("[*]Lutfen Taranacak Ana Bilgisayar Adresini Girin : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-v', '-Pn', '-sV','-oN','Port_Discover.txt', port])
    print('-' * 80)



def port_discoveryInRange():
    port = input("[*]Lutfen Taranacak Ana Bilgisayar Adresini Girin : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap','-p','1-100','-oN','Port_DiscoverInRange.txt', port])
    print('-' * 80)
 


def clear():
    os.system('cls||clear')




def quit_Program():
    quit()




if __name__ == '__main__':
    mainMenu()

