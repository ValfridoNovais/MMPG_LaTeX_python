from pylatex import Document, Section, Subsection, Itemize, Command, NoEscape
from pylatex.utils import bold

# Função para gerar o documento LaTeX
def generate_latex_document():
    # Criar o documento
    doc = Document('basic')

    # Adicionar o pacote minted ao documento
    #doc.packages.append(NoEscape(r'\usepackage{minted}'))

    # Adicionar os pacotes xcolor e minted ao documento
    doc.packages.append(NoEscape(r'\usepackage{xcolor}'))
    doc.packages.append(NoEscape(r'\usepackage{minted}'))

    # Título e autor
    doc.preamble.append(Command('title', 'Documentação do Projeto: Remoção de Fundo de Vídeos com OpenCV e MediaPipe'))
    doc.preamble.append(Command('author', 'Seu Nome'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    # Configuração para estilo "Dracula"
    doc.preamble.append(NoEscape(r'''
\usemintedstyle{colorful}
\definecolor{bg}{HTML}{282A36} % Fundo estilo Dracula
\definecolor{codegreen}{rgb}{0.0, 0.6, 0.0}
\definecolor{codegray}{rgb}{0.5, 0.5, 0.5}
\definecolor{codepurple}{rgb}{0.58, 0.0, 0.82}
\definecolor{backcolour}{rgb}{0.12, 0.12, 0.17}
\setminted{
    bgcolor=bg,
    frame=lines,
    framesep=2mm,
    baselinestretch=1.2,
    fontsize=\small,
    linenos=true,
    numbersep=5pt,
    tabsize=4,
    breaklines=true,
    escapeinside=||
}
'''))

    # Seção Introdução
    with doc.create(Section('Introdução')):
        doc.append("Este projeto tem como objetivo realizar a remoção do fundo de vídeos utilizando técnicas de "
                   "segmentação semântica com a biblioteca ")
        doc.append(bold("MediaPipe"))
        doc.append(", em conjunto com o ")
        doc.append(bold("OpenCV"))
        doc.append(" para processamento de vídeo. O resultado final preserva o objeto em primeiro plano "
                   "(geralmente uma pessoa) e substitui o fundo por uma cor sólida (branco, por padrão) ou outro tratamento desejado. "
                   "Além disso, o vídeo processado é salvo em formato MP4.")

    # Seção Tecnologias Utilizadas
    with doc.create(Section('Tecnologias Utilizadas')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item(bold("OpenCV") + ": Biblioteca para processamento de imagens e vídeos.")
            itemize.add_item(bold("MediaPipe") + ": Biblioteca do Google que fornece modelos de aprendizado de máquina prontos para segmentação de imagens e vídeos.")
            itemize.add_item(bold("NumPy") + ": Biblioteca para manipulação eficiente de arrays e matrizes numéricas.")

    # Seção Instalação e Configuração do Ambiente
    with doc.create(Section('Instalação e Configuração do Ambiente')):

        # Subseção Requisitos de Sistema
        with doc.create(Subsection('Requisitos de Sistema')):
            with doc.create(Itemize()) as itemize:
                itemize.add_item("Python 3.x")
                itemize.add_item("Sistema operacional: Windows, Linux, ou macOS")
                itemize.add_item("Ferramentas de linha de comando (ex: Git Bash ou terminal padrão)")

        # Subseção Bibliotecas Necessárias
        with doc.create(Subsection('Bibliotecas Necessárias')):
            doc.append("Para rodar este projeto, você precisa instalar algumas bibliotecas Python. "
                       "Você pode fazer isso utilizando o ")
            doc.append(bold("pip"))
            doc.append(" dentro do seu ambiente virtual. Execute os seguintes comandos no terminal:")

            doc.append(NoEscape(r"""
\begin{minted}[linenos]{bash}
pip install opencv-python
pip install numpy
pip install mediapipe
\end{minted}
"""))

        # Subseção Estrutura do Projeto
        with doc.create(Subsection('Estrutura do Projeto')):
            doc.append(NoEscape(r"""
\begin{verbatim}
MMPG-Background/
|
+-- video/
|   \-- video.mp4               # Vídeo original de entrada
+-- venv/                       # Ambiente virtual (opcional)
+-- main.py                     # Script principal do projeto
+-- .gitignore                  # Arquivos ignorados pelo Git
+-- LICENSE                     # Licença do projeto
\-- README.md                   # Instruções sobre o projeto
\end{verbatim}
"""))

    # Seção Descrição do Código
    with doc.create(Section('Descrição do Código')):

        # Subseção 1. Importação das Bibliotecas
        with doc.create(Subsection('1. Importação das Bibliotecas')):
            doc.append("O código começa com a importação das bibliotecas necessárias: ")
            doc.append(NoEscape(r"\texttt{cv2}"))
            doc.append(" (OpenCV), ")
            doc.append(NoEscape(r"\texttt{mediapipe}"))
            doc.append(" para segmentação, e ")
            doc.append(NoEscape(r"\texttt{numpy}"))
            doc.append(" para operações de arrays.")
            
            doc.append(NoEscape(r"""
\begin{minted}[linenos]{python}
import cv2
import mediapipe as mp
import numpy as np
\end{minted}
"""))

        # Subseção 2. Inicialização do MediaPipe
        with doc.create(Subsection('2. Inicialização do MediaPipe')):
            doc.append("Inicializamos o MediaPipe com o modelo de segmentação, que detecta a pessoa no vídeo.")
            
            doc.append(NoEscape(r"""
\begin{minted}[linenos]{python}
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)
\end{minted}
"""))

        # Subseção 3. Definição dos Caminhos de Arquivos
        with doc.create(Subsection('3. Definição dos Caminhos de Arquivos')):
            doc.append("Definimos os caminhos do vídeo de entrada e de saída. O vídeo de entrada deve estar localizado no caminho especificado:")
            
            doc.append(NoEscape(r"""
\begin{minted}[linenos]{python}
video_path = r'C:\\Caminho\\video.mp4'
output_path = r'C:\\Caminho\\video_processado.mp4'
\end{minted}
"""))

        # Subseção 4. Leitura e Escrita de Vídeos
        with doc.create(Subsection('4. Leitura e Escrita de Vídeos')):
            doc.append("O OpenCV é usado para ler o vídeo (")
            doc.append(NoEscape(r"\texttt{cv2.VideoCapture}"))
            doc.append(") e configurar a escrita do vídeo processado (")
            doc.append(NoEscape(r"\texttt{cv2.VideoWriter}"))
            doc.append("). O vídeo de saída mantém a resolução e o FPS (frames por segundo) do vídeo original.")
            
            doc.append(NoEscape(r"""
\begin{minted}[linenos]{python}
cap = cv2.VideoCapture(video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
\end{minted}
"""))

        # Subseção 5. Loop de Processamento de Frames
        with doc.create(Subsection('5. Loop de Processamento de Frames')):
            doc.append("Cada frame do vídeo é lido e processado em um loop. Para cada frame:")
            with doc.create(Itemize()) as itemize:
                itemize.add_item("Ele é convertido para o formato RGB, necessário pelo MediaPipe.")
                itemize.add_item("A segmentação de fundo é realizada.")
                itemize.add_item("O fundo é substituído por uma cor sólida (branco por padrão).")
            
            doc.append(NoEscape(r"""
\begin{minted}[linenos]{python}
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = segmentation.process(frame_rgb)
    mask = result.segmentation_mask > 0.5
    mask_3d = np.dstack((mask, mask, mask))
    person_segmented = np.where(mask_3d, frame, BACKGROUND_COLOR)
    person_segmented = person_segmented.astype(np.uint8)
    out.write(person_segmented)
    cv2.imshow('Fundo Removido com Cores Preservadas', person_segmented)
    if cv2.waitKey(30) & 0xFF == ord('q'): break
\end{minted}
"""))

        # Subseção 6. Finalização e Liberação de Recursos
        with doc.create(Subsection('6. Finalização e Liberação de Recursos')):
            doc.append("Ao final do processamento, o vídeo de saída é liberado e todas as janelas são fechadas:")
            
            doc.append(NoEscape(r"""
\begin{minted}[linenos]{python}
cap.release()
out.release()
cv2.destroyAllWindows()
\end{minted}
"""))

    # Seção Opções de Customização
    with doc.create(Section('Opções de Customização')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item(bold("Cor do Fundo") + ": A cor de fundo padrão é branco (255, 255, 255). "
                             "Você pode alterar isso ajustando a variável BACKGROUND_COLOR.")
            itemize.add_item(bold("Fundo Transparente") + ": Se desejar, pode implementar um fundo transparente usando máscaras alfa.")
            itemize.add_item(bold("Alteração de Resolução e FPS") + ": É possível alterar as propriedades do vídeo de saída definindo os parâmetros de resolução e taxa de quadros no cv2.VideoWriter.")

    # Seção Melhorias Futuras
    with doc.create(Section('Melhorias Futuras')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item(bold("Aplicação de IA Avançada") + ": Você pode explorar o uso de redes neurais mais robustas para obter segmentações mais precisas, especialmente em vídeos com cenários complexos.")
            itemize.add_item(bold("Integração com GUI") + ": Adicionar uma interface gráfica (usando Tkinter ou PyQt) pode facilitar o uso do programa por usuários não técnicos.")
            itemize.add_item(bold("Substituição de Fundo por Imagem/Outro Vídeo") + ": Pode-se substituir o fundo removido por uma imagem ou outro vídeo, simulando um efeito de 'chroma key'.")

    # Seção Erros Comuns e Soluções
    with doc.create(Section('Erros Comuns e Soluções')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item(bold("Erro ao carregar o vídeo") + ": Certifique-se de que o caminho para o vídeo de entrada esteja correto e o arquivo exista no local especificado.")
            itemize.add_item(bold("Problemas de exibição de vídeo (cv2.imshow)") + ": O OpenCV pode gerar erros ao exibir vídeos dependendo do formato. A conversão para uint8 é crucial para evitar problemas de exibição.")

    # Seção Licença
    with doc.create(Section('Licença')):
        doc.append("Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.")

    # Gerar o arquivo LaTeX
    doc.generate_tex('documentacao_projeto')

# Executar a função para gerar o documento
generate_latex_document()
