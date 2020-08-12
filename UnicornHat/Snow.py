import LEDMatrixSim
import time

width = 8
height = 4
changerandomly = False

def toggle_random():
    global changerandomly
    changerandomly = False if changerandomly else True

sim = LEDMatrixSim.Simulation(width,height)
btn_start = LEDMatrixSim.tkinter.Button(sim.Window, text="Rnd", width=4, command=toggle_random)
btn_start.grid(column=len(sim.Controls),row=height)

while True:
    if changerandomly:
        sim.change_random()
    sim.Window.update()
    time.sleep(0.05)
