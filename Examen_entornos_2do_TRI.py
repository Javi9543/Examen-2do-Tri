def agregar_tareas(tareas, titulo):
    for titulo in tareas:
        if titulo not in tareas:
            tareas.append("tarea4")
        
        tareas = {"titulo": titulo, "hecho":True}
        
        
def listar_tareas(tareas):
    print("-- Lista de Tareas --")
    for i in tareas:
        if i != tareas[True]:
            print(f'[] {i}')
        else:
            print(f'[x] {i}')
            
def contar_pendientes(tareas):
    contador = 0
    for i in tareas:
        if i == tareas[False]:
            contador += 1
        
    print("Numero de tareas Pendientes: ", contador)
            
            
def main():
    tarea1 = {"titulo": "Estudiar_python","hecho":False}
    tarea2 = {"titulo": "Hacer_Ejercicio", "hecho": True}
    tarea3 = {"titulo": "Leer 10 páginas", "hecho" : False}
    
    tareas = [tarea1, tarea2, tarea3]
    
    while True:
        try:
            print("-- Menu principal --")
            print(" 1 - Listar tareas")
            print(" 2 - Agregar tareas ")
            print(" 3 - Marcar hecha ")
            print(" 4 - Ver Tareas Pendientes " )
            print(" 5 - Salir ")
            
            opc = int(input("introduzca una opción del 1 - 4 (5 para salir): "))
            
            if opc == 1:   
                listar_tareas(tareas)
                input ("ENTER para continuar")
                
            elif opc == 2:
                nuevaTarea = input("Introduce el nombre de la tarea: ")
                agregar_tareas(tareas, nuevaTarea)
                input("Enter para continuar")
                
            elif opc == 3:
                print("en proceso...")
            
            elif opc == 4:
                contar_pendientes(tareas)
                input("Enter para continuar")
            
            elif opc == 5:
                print("Saliendo del programa...")
                break
        except ValueError:
            print("Introduzca solo numeros enteros")
    
if __name__ == "__main__":
    main()