import tempfile
import concurrent.futures 
from pypdf import PdfReader, PdfWriter 
from main import extrair

with tempfile.TemporaryDirectory() as path:
    leitor = PdfReader("teste.PDF")
    caminhos_saida = ["primeira_parte", "segunda_parte", "terceira_parte", "quarta_parte"]
    escritor1 = PdfWriter()
    escritor2 = PdfWriter()
    escritor3 = PdfWriter()
    escritor4 = PdfWriter()

    divisao = len(leitor.pages) // 4
    escritor1.append(leitor, pages=(0, divisao))
    escritor1.write(f'{caminhos_saida[0]}.pdf')

    escritor2.append(leitor, pages=(divisao, divisao * 2))
    escritor2.write(f'{caminhos_saida[1]}.pdf')

    escritor3.append(leitor, pages=(divisao * 2, divisao * 3))
    escritor3.write(f'{caminhos_saida[2]}.pdf')

    escritor4.append(leitor, pages=(divisao * 3, divisao * 4))
    escritor4.write(f'{caminhos_saida[3]}.pdf')

    if len(leitor.pages) >= 2:
        with concurrent.futures.ThreadPoolExecutor(4) as executor:
            futures = [executor.submit(extrair, f'{caminhos_saida[i]}.pdf', f'{caminhos_saida[i]}.txt') for i in range(4)]
            concurrent.futures.wait(futures)
    else:
        extrair(f'{caminhos_saida[1]}.pdf', f'{caminhos_saida[1]}.txt')
