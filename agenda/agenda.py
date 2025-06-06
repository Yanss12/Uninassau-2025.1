# Lista para guardar os contatos
agenda = []

def adicionar_contato(novo_contato: dict) -> None:
    '''
        Descrição: Função para adicionar novo contato na agenda(lista). /n
        Parâmetro: A função recebe um novo_contato do tipo dict. /n
        Retorno: A função não retorna nada.
    '''
    agenda.append(novo_contato)

def exibir_contatos() -> list:
    '''
        Descrição: Função para retornar os contatos da agenda(lista). /n
        Parâmetro: A função não recebe valores no parâmetro. /n 
        Retorno: A função retorna uma lista com todos os contatos.    
    '''
    return agenda

def atualizar_telefone(contato: str, novo_numero: str) -> bool:
    for contato in agenda:
        if contato['nome'] == contato:
            contato['telefone'] == novo_numero
            return True
        return False