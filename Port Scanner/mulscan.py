# Para execução em Windows é necessário ter instalado o Nmap. A instalação pode ser feita através do site: https://nmap.org/download.html
import nmap

scanner = nmap.PortScanner()

print("Bem vindo ao mulscan")
print("<------------------>\n")

ip = input("Digite o IP a ser verificado: ")

print("""Escolha o tipo de varredura a ser realizado
          1 -> SYN
          2 -> UDP
          3 -> Varredura Intensa
""")
scan_type = input("Digite a opção escolhida: ")

if scan_type == "1":
  print(f"\nVersão do Nmap {scanner.nmap_version()[0]}.{scanner.nmap_version()[1]}")

  scanner.scan(ip, "1-1024", "-v -sS")
  print("Informações do Scanner: ", scanner.scaninfo())
  print("Status do IP: ", scanner[ip].state())
  print("Protocolos:", end=" ")
  print(*scanner[ip].all_protocols())
  print("\nPortas Abertas: ", ", ".join(scanner[ip]["tcp"].keys()))

elif scan_type == "2":
  print(f"\nVersão do Nmap {scanner.nmap_version()[0]}.{scanner.nmap_version()[1]}")

  scanner.scan(ip, "1-1024", "-v -sU")
  print("Informações do Scanner: ", scanner.scaninfo())
  print("Status do IP: ", scanner[ip].state())
  print("Protocolos:", end=" ")
  print(*scanner[ip].all_protocols())
  print("\nPortas Abertas: ", ", ".join(scanner[ip]["udp"].keys()))

elif scan_type == "3":
  print(f"\nVersão do Nmap {scanner.nmap_version()[0]}.{scanner.nmap_version()[1]}")

  scanner.scan(ip, "1-1024", "-v -sC")
  print("Informações do Scanner: ", scanner.scaninfo())
  print("Status do IP: ", scanner[ip].state())
  print("Protocolos:", end=" ")
  print(*scanner[ip].all_protocols())
  print("\nPortas Abertas: ", ", ".join(scanner[ip]["tcp"].keys()))
else:
  print("Opção inválida")