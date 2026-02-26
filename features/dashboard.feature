Feature: Validação do DashBoard

  Scenario: Realize um movimento bancário, caixa e consulte saldo
    Given que o sistema Eco está aberto e logado
    When acesse a tela BAN004CA
    And cadastre um movimento no valor de R$ 250
    And acesse a tela CXA002CA
    And cadastre um lançamento no valor de R$ 500
    When acesse a tela GER212PA
    And clique no botão DRE
    Then o valor total do Caixa / Banco deve ser R$ 750,00
    Given eu clico no card Caixa / Banco
    Then valido os resumos superiores da tela de detalhes:
    | total_caixa | total_banco | total_geral |
    | R$ 500,00   | R$ 250,00   | R$ 750,00   |
    And valido que os seguintes saldos aparecem no grid:
    | descricao                            | saldo  |
    | BANCO EFI                            | 250,00 |
    | BANCO COOPERATIVO DO BRASIL S.A.     | 0,00   |
    | CAIXA PADRAO                         | 500,00 |