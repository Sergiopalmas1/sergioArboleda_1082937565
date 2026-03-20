estudiantes = ["Juan Camilo", "Juan Esteban", "Maria Paula", "María José", "Camilo" , "Adriana", "Laura", "Edwin", "Marcos ", 
"xavi "]
#agregar un nuevo estudiante a la lista
estudiantes.append("eider")
print(estudiantes)
estudiantes.append("Yarith")
print(estudiantes)
estudiantes.append("Juan gutierrez")
print(estudiantes)
                   
#imprimir la lista de estudiantes
print(estudiantes)

#obtener el número de estudiantes en la lista
print(len(estudiantes)) 

#buscar un estudiante en la lista
if "Juan Camilo" in estudiantes:
    print("Juan Camilo está en la lista de estudiantes")

#eliminar un estudiante de la lista
estudiantes.remove("Laura")
print(estudiantes)
