import pandas
from fpdf import FPDF

tabela_funcionarios = pandas.read_csv("base_dados_funcionarios.csv")

nome_empresa = "Marcelo e Sara Transportes Ltda"
cnpj_empresa = "01.336.733/0001-64"

for indice, info_funcionario in tabela_funcionarios.iterrows():
    nome_funcionario = info_funcionario.nome
    cpf_funcionario = info_funcionario.cpf
    salario_funcionario = info_funcionario.salario

    texto_recibo = f"Pelo presente, eu {nome_funcionario}\
  , inscrito no CPF sob nº {cpf_funcionario}, declaro que RECEBI\
  na data de hoje, o valor de R${salario_funcionario}, por meio de depósito\
    bancário, de {nome_empresa}, inscrito no \
    CNPJ sob nº {cnpj_empresa}, referente ao mês anterior \
    ao da data da assinatura, já incluindo todas as horas \
    devidas e benefícios."


    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "", 14)
    pdf.multi_cell(txt=texto_recibo, w=0, align="c")
    pdf.ln(30)

    pdf.cell(txt="Sendo expressão de verdade e sem qualquer \
    coação, firmo o presente.", w=0, align="c")
    pdf.ln(30)

    pdf.cell(txt="_______, __ de ______ de ____", w=0, align="c")
    pdf.ln(30)

    pdf.cell(txt="________________________________", w=0, align="c")
    pdf.ln()

    pdf.cell(txt=nome_funcionario, w=0, align="c")

    pdf.output(f"recibos/recibo_{nome_funcionario}.pdf")
