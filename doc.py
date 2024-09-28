from pylatex import Document, Section, Subsection, Command, Tabular
from pylatex.utils import NoEscape

# Criar o documento
doc = Document()

# Adicionar conteúdo ao documento
with doc.create(Section('Introdução')):
    doc.append('Este é um exemplo simples de um documento gerado com PyLaTeX. ')
    
    with doc.create(Subsection('Tabela Exemplo')):
        doc.append('Abaixo está uma tabela de exemplo:')
        
        # Criar uma tabela com 2 colunas
        with doc.create(Tabular('c|c')) as table:
            table.add_hline()
            table.add_row(('Coluna 1', 'Coluna 2'))
            table.add_hline()
            table.add_row((1, 2))
            table.add_row((3, 4))
            table.add_hline()

# Gerar o arquivo LaTeX
doc.generate_tex('exemplo_documento')

# Também é possível gerar o PDF automaticamente, se você tiver o compilador LaTeX configurado
doc.generate_pdf('exemplo_documento', clean_tex=False)
