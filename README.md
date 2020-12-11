# First Order Differenital Equation Approximator


---

### Table of Contents


- [Description](#description)
- [Dependencies](#Dependencies)
- [How To Use](#how-to-use)
- [Testing for those who do not understand approximating differential equations](#Testing)
- [Author Info](#author-info)

---

## Description

This Program is intended to approximate first order ordinary differential equations using a select range of numerical methods when analytical methods will not suffice. It is able to approximate using the Euler method, Heun method and Runge-Kutta method. It is able to plot each approximate solution and also save the y-axis values, along with their corresponding t-axis counterparts. 

---

## Dependencies

- Tkinter
- Numpy
- Matplotlib



---

## How To Use

#### Installation

If you have installed all the dependencies, running the 'src.py' file will work as long as you have it in the same directory as 'ico.ico' and 'dydt.gif'. If you want to compile the file yourself, open the terminal in the source file directory and enter the following command

```cmd
pyinstaller -F -w -i "ico.ico" src.py
```
The executable will be in the generated "dist" folder but you will need to take it out and put it in same folder as 'ico.ico' and 'dydt.gif' before running. 

### Inputting a differential equation and using Trigonometric functions or powers

When inputting differntial equations, you must isolate all expressions that do not contain dy/dt on the right hand side. For example, if your equation is 2dy/dt+5t=y this becomes dy/dt=(y-5*t)/2


##### Using trigonometric functions

When using a trigonometric function, it is important to write 'np.' at the front, in reference to Numpy. 
For example, if your differential equation is
dy/dt=2sin(t)
you would input dy/dt = ``` 2*np.sin(t) ``` into the program. 

##### Using powers

When using powers, it is denoted as '**'.
For example, if your differential equation is
dy/dt = ty^2,
you would input dy/dt = ``` t*y**2 ``` into the program input. 

---

## Testing 

If you want to test the program by plotting f(x) = e^x this can be easily done.
In the program, enter the following inputs in the input boxes.
Step size = 0.1 -> dy/dx = y -> y0 = 1 -> From t = 0 -> To t = 5.

This program is meant for differential equations that cannot be solved analytically but approximating dy/dx = y shows the capabilites of the software by producing a graph very similar to f(x) = e^x.

---


## Author Info

- Name - Alex Shomali
- Email - alexshomali123@gmail.com


