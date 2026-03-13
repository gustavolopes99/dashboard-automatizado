Feature: Validação do DashBoard

  Background:
    Given zerar o banco de dados
    And cadastrar a conta
    And autonomias liberadas
    
 Scenario: Consulte os valores informados em Caixa / Banco
    Given que os seguintes lançamentos de caixa são injetados no banco de dados:
      | historico | valordh | valorch |
      | 01        | 500,00  | 0,00    |
      | 28        | 800,00  | 0,00    |
      | 30        | 0,00    | 125,30  |
    And que os seguintes movimentos bancários são injetados no banco de dados:
      | conta | valor | operacao | conciliado |
      | 01    | 515   | 04       | S          |
      | 01    | 109   | 07       | S          |
      | 01    | 91    | 04       | N          |
    When abrir o sistema eco e realize login
    And acesse a tela DSH001PA
    #Then valide os graficos de caixa e banco:
    #  | caixa   | banco  | 
    #  | 1450,25 | 250,00 | 
    Then o valor total do Caixa / Banco deve ser R$ 1.922,30
    When eu clico no card Caixa / Banco
    #Then valide o gráfico Saldo total (implantar)
    #And valide o gráfico Caixa por tipo de saldo (implantar)
    #And valide o gráfico Banco por tipo de saldo (implantar)
    And valide os resumos superiores da tela de detalhes de caixa e banco:
    | total_caixa  | total_banco | total_geral |
    | R$ 1.425,30  | R$ 497,00   | R$ 1.922,30 |
    And valide os seguintes saldos aparecem no grid:
    | descricao          | nosso_saldo | saldo_banco | saldo_geral | saldo_dinheiro | saldo_cheque | saldo_caixa |
    | BANCO DO BRASIL SA | 497,00      | 406,00      | 497,00      | -              | -            | -           |
    | CAIXA PADRAO       | -           | -           | -           | 1300,00        | 125,30       | 1425,30     |
  
  @dashboard @squad_financeiro
  Scenario: Consulte os valores informados em Contas a receber
    Given cliente cadastrado
    Given que os seguintes documentos a receber são injetados no banco de dados:
      | valor   | qtd_parc | emissao    |
      | 500,00  |  2       | hoje       |
      | 250,25  |  1       | anopassado |
      | 6000,00 |  5       | mesquevem  |
    When abrir o sistema eco e realize login
    And acesse a tela DSH001PA
    Then valide os graficos a receber:
      | vencidos | venc_hoje | a_vencer |
      | 1450,25  |  250,00   | 5050,00  |
    And o valor total do Contas a receber deve ser R$ 6.750,25
    And eu clico no card Contas a receber
    #Then valide o gráfico maior volume de vencidos (implantar)
    #And valide o gráfico maior volume vencendo hoje (implantar)
    #And valide o gráfico maior volume a vencer (implantar)
    #And valide o gráfico documentos por portador (implantar)
    And os totalizadores superiores devem corresponder a soma das colunas da tabela