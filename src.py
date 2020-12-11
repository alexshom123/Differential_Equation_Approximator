#credits
__author__ = "Alex Shomali"
__version__= "1.2"

#imports
import tkinter
import matplotlib.pyplot as plt
import numpy as np

#gui class
class ProgramGUI:

    def __init__(self):
        #Creates the initial window
        self.main = tkinter.Tk()
        self.main.resizable(width=False, height=False)
        self.main.title('First Order Differential Equation Approximator')
        self.main.iconbitmap('ico.ico')
        #Defines a few vairables which are used in the form
        self.dydt = tkinter.StringVar()
        self.tn = tkinter.StringVar()
        self.yn = tkinter.StringVar()
        self.tEnd = tkinter.StringVar()
        self.h = tkinter.StringVar()

        #Creates the frames
        self.dyFrame = tkinter.Frame(self.main)
        
        self.stepsFrame = tkinter.Frame(self.main)
        self.stepsFrameA = tkinter.Frame(self.stepsFrame)
        self.stepsFrameB = tkinter.Frame(self.stepsFrame)
        
        self.tFrames = tkinter.Frame(self.main)
        self.tFramesA = tkinter.Frame(self.tFrames)
        self.tFramesB = tkinter.Frame(self.tFrames)

        #Creates and packs the title label
        tkinter.Label(self.main, text="-- First Order Differential Equation Approximator -- ", font=("Arial", 14), fg="Blue").pack()

        #Adds stuff to the dyFrame
        self.dyImage = tkinter.PhotoImage(file="dydt.gif")
        tkinter.Label(self.dyFrame, image=self.dyImage).pack(side='left')
        tkinter.Entry(self.dyFrame, width=35, textvariable=self.dydt).pack(side='left')

        self.dyFrame.pack()

        #Adds stuff to stepsFrameA
        tkinter.Label(self.stepsFrameA, text='Step Size =  ').pack(side = 'left')
        tkinter.Entry(self.stepsFrameA, width=4, textvariable=self.h).pack(side='left')
        tkinter.Label(self.stepsFrameA, text='                                      ').pack(side = 'left')

        self.stepsFrameA.pack(side = 'left')

        tkinter.Label(self.stepsFrameB, text='y0 =  ').pack(side = 'left')
        tkinter.Entry(self.stepsFrameB, width=4, textvariable=self.yn).pack(side='left')

        self.stepsFrameB.pack(side = 'left')

        self.stepsFrame.pack()


        #Adds stuff to stepsFrameA
        tkinter.Label(self.tFramesA, text='   From t =   ').pack(side = 'left')
        tkinter.Entry(self.tFramesA, width=4, textvariable=self.tn).pack(side='left')
        tkinter.Label(self.tFramesA, text='                                   ').pack(side = 'left')

        self.tFramesA.pack(side = 'left')

        tkinter.Label(self.tFramesB, text=' To t = ').pack(side = 'left')
        tkinter.Entry(self.tFramesB, width=4, textvariable=self.tEnd).pack(side='left')

        self.tFramesB.pack(side = 'left')

        self.tFrames.pack()

        #Creates 3 buttons and adds them to the button frame
        tkinter.Button(self.main, text="            Plot Euler Approximation          ",command=lambda:(self.mainFunc())).pack(side="bottom",pady=4)
        tkinter.Button(self.main, text="         Plot Heun Approximation            ",command=lambda:(self.mainFunc2())).pack(side="bottom",pady=4)
        tkinter.Button(self.main, text="   Plot Runge-Kutta Approximation     ",command=lambda:(self.mainFunc3())).pack(side="bottom",pady=4)
        

        #Creates the main loop of the program
        self.main.mainloop()

    #Function for Euler's method
    def mainFunc(self):
        try:
            #cast as float and close plot each time button in pressed
            plt.close('all')
            self.tn_sent = float(self.tn.get())
            self.tEnd_sent = float(self.tEnd.get())
            self.h_sent = float(self.h.get())
            self.yn_sent = float(self.yn.get())

            self.tVals = [self.tn_sent]
            self.yVals = [self.yn_sent]
            #preform eulers method
            while (self.tn_sent < self.tEnd_sent):
                self.function = eval(self.dydt.get().replace('t', 'self.tn_sent').replace('y', 'self.yn_sent'))
                self.yn_sent = self.yn_sent + self.h_sent*self.function
                self.tn_sent = self.tn_sent+self.h_sent
                self.tVals.append(round(self.tn_sent,4))
                self.yVals.append(round(self.yn_sent,4))
            #throw error for invalid input
            if len(self.tVals) < 2 and  len(self.yVals) < 2:
                tkinter.messagebox.showerror('Error',"Invalid input")
            else: 
                plt.plot(self.tVals, self.yVals,'r--',linewidth=2,label='Approx')
                plt.title("Euler approximation for y(t)")
                plt.xlabel("t")
                plt.ylabel("y(t)")
                plt.legend()
                plt.show(block=False)
                tkinter.messagebox.showinfo('Success!',"Approximate solution plotted. The t and y values have been saved to 'Latest_Approximation_Values.txt'")
               
        except:
            tkinter.messagebox.showerror('Error',"Invalid Input")

        #File I/O
        with open('Latest_Approximation_Values.txt', 'w') as file_handler:
            file_handler.write(f"\ny_values\n")
            for item in self.yVals:
                file_handler.write("{}\n".format(item))

        with open('Latest_Approximation_Values.txt', 'a') as file_handler:
            file_handler.write("\nt_values\n")
            for item in self.tVals:
                file_handler.write("{}\n".format(item))

    #Function for Heuns method            
    def mainFunc2(self):
        try:
            #cast as float and close plot each time button in pressed
            plt.close('all')
            self.tn_sent = float(self.tn.get())
            self.tEnd_sent = float(self.tEnd.get())
            self.h_sent = float(self.h.get())
            self.yn_sent = float(self.yn.get())

            self.tVals = [self.tn_sent]
            self.yVals = [self.yn_sent]
            #preform Heuns method
            while (self.tn_sent < self.tEnd_sent):
                self.k1 = eval(self.dydt.get().replace('t', 'self.tn_sent').replace('y', 'self.yn_sent'))
                self.k2 = eval(self.dydt.get().replace('t', 'self.tn_sent+self.h_sent').replace('y', 'self.yn_sent+self.h_sent*self.k1'))
                self.yn_sent = self.yn_sent + (self.h_sent/2)*(self.k1+self.k2)
                self.tn_sent = self.tn_sent+self.h_sent
                self.tVals.append(round(self.tn_sent,4))
                self.yVals.append(round(self.yn_sent,4))
            #throw error for invalid input
            if len(self.tVals) < 2 and  len(self.yVals) < 2:
                tkinter.messagebox.showerror('Error',"Invalid input")
            else: 
                plt.plot(self.tVals, self.yVals,'b--',linewidth=2,label='Approx')
                plt.title("Heun approximation for y(t)")
                plt.xlabel("t")
                plt.ylabel("y(t)")
                plt.legend()
                plt.show(block=False)
                tkinter.messagebox.showinfo('Success!',"Approximate solution plotted. The t and y values have been saved to 'Latest_Approximation_Values.txt'")
               
        except:
            tkinter.messagebox.showerror('Error',"Invalid Input")

        #File I/O
        with open('Latest_Approximation_Values.txt', 'w') as file_handler:
            file_handler.write(f"\ny_values\n")
            for item in self.yVals:
                file_handler.write("{}\n".format(item))

        with open('Latest_Approximation_Values.txt', 'a') as file_handler:
            file_handler.write("\nt_values\n")
            for item in self.tVals:
                file_handler.write("{}\n".format(item))

    #Function for Runge Kutta method
    def mainFunc3(self):
        try:
            #cast as float and close plot each time button in pressed
            plt.close('all')
            self.tn_sent = float(self.tn.get())
            self.tEnd_sent = float(self.tEnd.get())
            self.h_sent = float(self.h.get())
            self.yn_sent = float(self.yn.get())

            self.tVals = [self.tn_sent]
            self.yVals = [self.yn_sent]
            #preform Heuns method
            while (self.tn_sent < self.tEnd_sent):
                self.k1 = eval(self.dydt.get().replace('t', 'self.tn_sent').replace('y', 'self.yn_sent'))
                self.k2 = eval(self.dydt.get().replace('t', 'self.tn_sent+0.5*self.h_sent').replace('y', 'self.yn_sent+0.5*self.h_sent*self.k1'))
                self.k3 = eval(self.dydt.get().replace('t', 'self.tn_sent+0.5*self.h_sent').replace('y', 'self.yn_sent+0.5*self.h_sent*self.k2'))
                self.k4 = eval(self.dydt.get().replace('t', 'self.tn_sent+self.h_sent').replace('y', 'self.yn_sent+self.h_sent*self.k3'))
                self.yn_sent = self.yn_sent + (self.h_sent/6)*(self.k1+2*self.k2+2*self.k3+self.k4)
                self.tn_sent = self.tn_sent+self.h_sent
                self.tVals.append(round(self.tn_sent,4))
                self.yVals.append(round(self.yn_sent,4))
            #throw error for invalid input
            if len(self.tVals) < 2 and  len(self.yVals) < 2:
                tkinter.messagebox.showerror('Error',"Invalid input")
            else: 
                plt.plot(self.tVals, self.yVals,'g--',linewidth=2,label='Approx')
                plt.title("Runge-Kutta approximation for y(t)")
                plt.xlabel("t")
                plt.ylabel("y(t)")
                plt.legend()
                plt.show(block=False)
                tkinter.messagebox.showinfo('Success!',"Approximate solution plotted. The t and y values have been saved to 'Latest_Approximation_Values.txt'")
               
        except:
            tkinter.messagebox.showerror('Error',"Invalid Input")

        #File I/O
        with open('Latest_Approximation_Values.txt', 'w') as file_handler:
            file_handler.write(f"\ny_values\n")
            for item in self.yVals:
                file_handler.write("{}\n".format(item))

        with open('Latest_Approximation_Values.txt', 'a') as file_handler:
            file_handler.write("\nt_values\n")
            for item in self.tVals:
                file_handler.write("{}\n".format(item))
                        
#main + start program
def main():
    gui = ProgramGUI()

if __name__ == '__main__':
    main()
