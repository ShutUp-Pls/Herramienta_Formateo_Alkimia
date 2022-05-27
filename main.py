import tkinter

NAME_PROG_1 = "Office 2019"

def iniciar_app():
    ventana = tkinter.Tk()
    ventana.geometry("300x300")
    ventana.title("Programas Escenciales")
    ventana.columnconfigure(0,weight=1)
    ventana.rowconfigure(0,weight=1)
    ventana.rowconfigure(1,weight=1)

    frame_prog_1 = tkinter.Frame(ventana, background="red")
    frame_prog_1.grid(row=0,column=0,sticky="nsew")

    frame_prog_2 = tkinter.Frame(ventana, background="blue")
    frame_prog_2.grid(row=1,column=0,sticky="nsew")

    ventana.mainloop()

iniciar_app()
