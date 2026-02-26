Feature: Validação do DashBoard

  Scenario: Realize um movimento bancário, caixa e consulte saldo
    Given que o sistema Eco está aberto e logado
    #When acesse a tela BAN004CA
    #And cadastre um movimento no valor de R$ 250
    #And acesse a tela CXA002CA
    #And cadastre um lançamento no valor de R$ 500
    When acesse a tela GER212PA
    And clique no botão DRE
    Then valide os detalhes do total de caixa/banco
    #Then o valor total do Caixa / Banco deve ser R$ 750,00
  
  # Scenario: Realize um lançamento de caixa e consulte o valor de caixa
