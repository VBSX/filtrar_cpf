import pyperclip as clipboard
from cpf_filter import CpfFilter
from get_cpf import CpfGetFile
from validate_docbr import CPF
def colocar_cpf_no_arquvio(lista_cpf_filtrado, arquivo_saida):
    with open(arquivo_saida, 'w') as file:
        for cpf in lista_cpf_filtrado:
            file.write(cpf + '\n')
    
cpf = CpfGetFile()
cpf.open_txt()
cpf.cpf_on_list(cpf.open_txt())



cpf_filter = CpfFilter(cpf.cpf_list)
cpf_filtrado = cpf_filter.filter()

print(cpf_filtrado)

print(cpf_filter.cont_cpf_filtered())

colocar_cpf_no_arquvio(cpf_filtrado, 'cpf_filtrado.txt')
list_text = f'{cpf_filtrado}'
clipboard.copy(list_text)


list_cpf_invalido = []
contagem = 0
for cpf in cpf_filtrado:
    
    if CPF().validate(cpf):
        print(f'O CPF {cpf} é válido.')
    else:
        print(f'O CPF {cpf} é inválido.')
        list_cpf_invalido.append(cpf)
        contagem += 1

print(list_cpf_invalido)
print(contagem)



        
        