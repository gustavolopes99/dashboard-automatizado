import sys
import firebirdsql as fdb

def inserir_usuario(arquivoSQL):
    with open(arquivoSQL, 'r') as arquivo:
        try:
            con = fdb.connect(
                host='localhost',
                database='C:/ecosis/dados/ecodados.eco',
                port=3050,
                user='sysdba',
                password='masterkey')
            
            cur = con.cursor()
            cur.execute("INSERT INTO TGerUsuario (Usuario, Nome, Ativo, Senha, IDusuario) VALUES ('TESTCOMPLETE', 'TESTCOMPLETE', 'S', '71633dcb3ab3f8e0940e94b0e6022283e6db7699', '06')")
            cur.execute("UPDATE tgerlicencamodulos m SET m.liberado = 'S'")
            cur.execute("UPDATE TORDPARAMETRO SET ELETRO='S', MOTOR='S', OUTROS='S', VEICULO='S' WHERE EMPRESA='01'")

            print(" * Usuário inserido")
            
            for linha in arquivo:
                cur.execute(linha)
            print(" * Módulos liberados para o usuário")
            
            con.commit()
            con.close()
            print(" * Concluido")
        except ValueError:
            print("error: ")
            
if __name__ == '__main__':
    arquivoSQL = sys.argv[1] + r'Certificacao\ecoTestCompleteBDD\ProjetoEco\Scripts_Banco\liberar_modulos_usuario.sql'
    inserir_usuario(arquivoSQL)