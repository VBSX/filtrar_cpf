class CpfFilter():
    def __init__(self, cpf_list):
        self.cpf_list = cpf_list
        self.cpf_list_filtered = []
        
    def filter(self):
        for cpf in self.cpf_list:

            cpf_filtered = cpf.replace('.', '').replace('-', '').replace(' ', '')
            self.cpf_list_filtered.append(cpf_filtered)
        return self.cpf_list_filtered
    
    def cont_cpf_filtered(self):
        return len(self.cpf_list_filtered)
    
    
if __name__ == '__main__':
    c= CpfFilter(['111.111.111-11', '222.222.222-22', '333.333.333-33'])
    print(c.filter())
    


        