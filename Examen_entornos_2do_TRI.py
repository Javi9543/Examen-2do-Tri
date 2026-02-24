def agregar_tareas(tareas, titulo):
    for titulo in tareas:
        if titulo not in tareas:
            tareas.append("tarea4")
        
        tareas = {"titulo": titulo, "hecho":False}
        
        
def listar_tareas(tareas):
    print("-- Lista de Tareas --")
    for i in tareas:
        print (i)
            
def main():
    tarea1 = {"titulo": "Estudiar_python","hecho": False}
    tarea2 = {"titulo": "Hacer_Ejercicio", "hecho": True}
    tarea3 = {"titulo": "Leer 10 páginas", "hecho" : False}
    
    tareas = [tarea1, tarea2, tarea3]
    
    
    nuevaTarea = input("Introduce el nombre de la tarea: ")
    agregar_tareas(tareas, nuevaTarea)
    
    listar_tareas(tareas)
if __name__ == "__main__":
    main()