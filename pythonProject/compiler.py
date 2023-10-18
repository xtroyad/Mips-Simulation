class Compiler:
    def __init__(self):
        pass

    def compile(self, circuit):

        file_name = "program.txt"

        try:
            with open(file_name, "r") as file:
                # Guardamos los datos en memoria
                for line in file:
                    cleaned_line = line.strip()
                    if (cleaned_line != ".data"):
                        break

                for line in file:
                    cleaned_line = line.strip()
                    data = line.strip()

                    if cleaned_line == ".text":
                        break

                    if (data != ''):
                        data = data.replace(",", "").replace(":", "").split() # Todo: que ha pasado

                        circuit.dataMem.add(data)
                label = ""
                # Guardamos las intrucciones en memoria
                for line in file:

                    instruction = line.strip()

                    if (instruction != ''):
                        instruction = instruction.replace(",", "")

                        elements = instruction.split()


                        # Hemos encontrado anteriormente una etiqueta
                        if not elements[0].endswith(":") and label != "":
                            circuit.instMem.addLabel(elements, label)
                            label = ""
                        elif not elements[0].endswith(":"):
                            circuit.instMem.add(elements)

                        # Instruc y etiqueta en distinta linea
                        if elements[0].endswith(":") and len(elements) == 1:
                            label = elements[0].replace(":", "")

                        # Intruc y etiqueta en la misma linea
                        if elements[0].endswith(":") and len(elements) > 1:
                            label = elements[0].replace(":", "")
                            elements.pop(0)
                            circuit.instMem.addLabel(elements, label)
                            label = ""



                        # Intruccion com formato lw $t0, n
                        if elements[0] == "lw" and elements[2] in circuit.dataMem.table:

                            offset = circuit.dataMem.table[elements[2]]

                            elements1 = ["add", "$at", "$zero", "$zero"]
                            elements2 = ["lw", str(offset), "$at"]

                            circuit.instMem.replacePseudoIntruc([elements1, elements2])

                        # El compilador cambia la instruccion li
                        if elements[0] == "li":

                            elements1 = ["addi", elements[1], "$zero", elements[2]]

                            circuit.instMem.replacePseudoIntruc([elements1])



        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Cambiamos las etiquetas de salto a inmediato

        for (dir, instruc) in circuit.instMem.content.items():
            if instruc == []:
                break

            if instruc[-1] in circuit.instMem.labels:
                dirLabel = circuit.instMem.labels[instruc[-1]]

                n = (dirLabel- dir)// 4 - 1
                instruc[-1] = n
                circuit.instMem.content[dir] = instruc
