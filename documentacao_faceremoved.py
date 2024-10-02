from pylatex import Document, Section, Subsection, Command, Enumerate, NoEscape
from pylatex.utils import italic, bold

def create_document():
    # Criando documento
    doc = Document('codigo_documentacao')

    # Adicionando título
    doc.preamble.append(Command('title', 'Documentação dos Códigos: Inicial e Melhorado'))
    doc.preamble.append(Command('author', 'Especialista Python'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    # Introdução
    with doc.create(Section('Introdução')):
        doc.append('Esta documentação descreve dois códigos, "CODIGO INICIAL" e "CODIGO MELHORADO", que realizam a detecção de faces usando MediaPipe. '
                   'Ambos os códigos capturam imagens da webcam, detectam faces e salvam fotos de intrusos. O "CODIGO MELHORADO" introduz melhorias no reconhecimento facial e na gestão de arquivos.')
    
    # Documentação do CODIGO INICIAL
    with doc.create(Section('Documentação do CODIGO INICIAL')):
        doc.append('O "CODIGO INICIAL" é responsável por detectar uma face na tela e salvar fotos de intrusos quando uma face diferente da memorizada é detectada.')

        with doc.create(Subsection('1. Importação de Bibliotecas')):
            doc.append('O código começa importando as bibliotecas essenciais: OpenCV para captura de vídeo, MediaPipe para a detecção de malhas faciais, '
                       'Numpy para cálculos numéricos e outras bibliotecas para manipulação de arquivos e tempo.')
        
        with doc.create(Subsection('2. Funções de Comparação e Memorização de Faces')):
            doc.append('As funções criadas no código incluem:')
            with doc.create(Enumerate()) as enum:
                enum.add_item('`compare_faces()`: Compara duas faces baseadas nos pontos de referência detectados.')
                enum.add_item('`ask_memorize_face()`: Abre um popup perguntando se o usuário deseja memorizar uma face detectada.')
                enum.add_item('`create_directory_structure()`: Cria pastas para armazenar as imagens, organizando por ano, mês e dia.')
                enum.add_item('`save_intruder_photo()`: Salva a imagem do intruso detectado.')
                enum.add_item('`save_memorized_photo()`: Salva a imagem de uma face memorizada.')
        
        with doc.create(Subsection('3. Captura e Processamento de Vídeo')):
            doc.append('O código inicializa a webcam com `cv2.VideoCapture(0)` e processa cada frame, detectando faces e desenhando a malha facial com MediaPipe. '
                       'Se uma face for detectada, o código compara com as faces memorizadas e salva a imagem do intruso, se for uma face nova.')

    # Documentação do CODIGO MELHORADO
    with doc.create(Section('Documentação do CODIGO MELHORADO')):
        doc.append('O "CODIGO MELHORADO" aprimora o processo de detecção e gerenciamento de faces. Ele adiciona suporte para múltiplas faces, melhorias na comparação facial e armazenamento de imagens.')

        with doc.create(Subsection('1. Alterações Importantes')):
            doc.append('O código foi modificado para detectar múltiplas faces, armazenar várias faces memorizadas e garantir que apenas faces não memorizadas sejam salvas como intrusas.')

        with doc.create(Subsection('2. Detecção de Múltiplas Faces')):
            doc.append('`max_num_faces` foi ajustado para detectar várias faces simultaneamente, aumentando a robustez do sistema.')

        with doc.create(Subsection('3. Gerenciamento de Faces Memorizadas')):
            doc.append('Agora, múltiplas faces podem ser memorizadas e o código consegue comparar a face detectada com todas as memorizadas antes de salvar como intruso.')

    # Comparação entre os Códigos
    with doc.create(Section('Comparação entre o CODIGO INICIAL e CODIGO MELHORADO')):
        doc.append('As principais diferenças entre os dois códigos estão no tratamento de múltiplas faces e na otimização do processo de comparação e salvamento de imagens.')
        with doc.create(Enumerate()) as enum:
            enum.add_item('Suporte para múltiplas faces no "CODIGO MELHORADO".')
            enum.add_item('Armazenamento eficiente de imagens organizadas por data e hora.')
            enum.add_item('Maior precisão na comparação de faces.')

    doc.generate_pdf('codigo_documentacao', clean_tex=False)

# Gerar documentação
create_document()
