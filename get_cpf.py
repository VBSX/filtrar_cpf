
class CpfGetFile():
    def __init__(self) -> None:
        self.file = 'cpfs.txt'
        self.cpf_list = []
    def open_txt(self):
        with open(self.file, 'r') as f:
            cpfs = f.read()
        return cpfs
    
    def cpf_on_list(self, txt):
        for cpf in txt.split('\n'):
            cpf = cpf.strip()  # Remove espaços em branco no começo e no fim
            if cpf:
                self.cpf_list.append(cpf)
    

if __name__ == '__main__':
    cpf = CpfGetFile()
    cpf.cpf_on_list(cpf.open_txt())
    print(cpf.cpf_list)
    
