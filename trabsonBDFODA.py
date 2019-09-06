import pymysql
import pymysql.cursors
import time

con = pymysql.connect(host='localhost',
	user='usuário1',
	password='12345',
	db='DBTarefas',
	charset='utf8',
	cursorclass=pymysql.cursors.DictCursor
	)
try:
	with con:
	 opção = 0
	 while opção != 4:

			print('1. Adicionar tarefa')
			print('2. Mostrar lista')
			print('3. Concluir tarefa')
			print('4. Remover tarefa')
			print('5. Sair')
			opção = int(input("Insira a opcao desejada: "))
			cur= con.cursor()

			if opção == 1:
				print('Criando nova tarefa')
				da = time.strftime('%Y-%m-%d %H:%M')
				Descrição = input("insira desc. da tarefa: ")
				Prioridade = input("Prioridade, podendo ser 1,2 ou 3): ")
				Concluído = "nao"
				cur.execute("INSERT INTO Tarefas (Descrição, Prioridade, Data, Concluído) VALUES ('"+Descrição+"','"+Prioridade+"','"+da+"','"+Concluído+"')")

			if opção == 2:
				cur.execute("SELECT * FROM Tarefas")
				rows = cur.fetchall()
				print("Tarefas: ")
				print("| Id | Descrição | Data | Prioridade | Concluído |")
				for row in rows:
					print("Tarefas: ")
					print("|",row["Id"],"|", row["Descrição"],"|", row["Data"],"|", row["Prioridade"],"|", row["Concluído"],"|")


			if opção == 3:
				idc=input("Insira o id da tarefa que dejeja marcar como concluida: ")
				cur = con.cursor()
				cur.execute("UPDATE Tarefas SET Concluído='sim' WHERE id='"+idc+"'")

			if opção == 4:
				idd=input("Insira o id da tarefa que você deseja excluir: ")
				cur.execute("DELETE FROM Tarefas WHERE id = '"+idd+"' ")

finally:
    con.close()
