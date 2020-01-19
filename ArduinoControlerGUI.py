#https://realpython.com/arduino-python/
#https://github.com/tino/pyFirmata#usage

from tkinter import Label, Button, Radiobutton, messagebox
import tkinter as tk
import sys, pyfirmata

class GUI_COntroller:
    '''
	   This class initialize the required controls for TkInter GUI
	'''

    def __init__(self, TkObject):

        self.syncWithBoardOnce = False
        self.dig_pin0_prev_status = tk.IntVar()
        self.dig_pin0 = tk.IntVar()
        self.dig_pin1_prev_status = tk.IntVar()
        self.dig_pin1 = tk.IntVar()
        self.dig_pin2_prev_status = tk.IntVar()
        self.dig_pin2 = tk.IntVar()
        self.dig_pin3_prev_status = tk.IntVar()
        self.dig_pin3 = tk.IntVar()
        self.dig_pin4_prev_status = tk.IntVar()
        self.dig_pin4 = tk.IntVar()
        self.dig_pin5_prev_status = tk.IntVar()
        self.dig_pin5 = tk.IntVar()
        self.dig_pin6_prev_status = tk.IntVar()
        self.dig_pin6 = tk.IntVar()
        self.dig_pin7_prev_status = tk.IntVar()
        self.dig_pin7 = tk.IntVar()
        self.dig_pin8_prev_status = tk.IntVar()
        self.dig_pin8 = tk.IntVar()
        self.dig_pin9_prev_status = tk.IntVar()
        self.dig_pin9 = tk.IntVar()
        self.dig_pin10_prev_status = tk.IntVar()
        self.dig_pin10 = tk.IntVar()
        self.dig_pin11_prev_status = tk.IntVar()
        self.dig_pin11 = tk.IntVar()
        self.dig_pin12_prev_status = tk.IntVar()
        self.dig_pin12 = tk.IntVar()
        self.dig_pin13_prev_status = tk.IntVar()
        self.dig_pin13 = tk.IntVar()

        self.dig_pin0_radio_status = None
        self.dig_pin0_radio_off_status = None
        self.dig_pin1_radio_status = None
        self.dig_pin1_radio_off_status = None
        self.dig_pin2_radio_status = None
        self.dig_pin2_radio_off_status = None
        self.dig_pin3_radio_status = None
        self.dig_pin3_radio_off_status = None
        self.dig_pin4_radio_status = None
        self.dig_pin4_radio_off_status = None
        self.dig_pin5_radio_status = None
        self.dig_pin5_radio_off_status = None
        self.dig_pin6_radio_status = None
        self.dig_pin6_radio_off_status = None
        self.dig_pin7_radio_status = None
        self.dig_pin7_radio_off_status = None
        self.dig_pin8_radio_status = None
        self.dig_pin8_radio_off_status = None
        self.dig_pin9_radio_status = None
        self.dig_pin9_radio_off_status = None
        self.dig_pin10_radio_status = None
        self.dig_pin10_radio_off_status = None
        self.dig_pin11_radio_status = None
        self.dig_pin11_radio_off_status = None
        self.dig_pin12_radio_status = None
        self.dig_pin12_radio_off_status = None
        self.dig_pin13_radio_status = None
        self.dig_pin13_radio_off_status = None

        self.digital_pin0_input = 0
        self.digital_pin1_input = 0
        self.digital_pin2_input = 0
        self.digital_pin3_input = 0
        self.digital_pin4_input = 0
        self.digital_pin5_input = 0
        self.digital_pin6_input = 0
        self.digital_pin7_input = 0
        self.digital_pin8_input = 0
        self.digital_pin9_input = 0
        self.digital_pin10_input = 0
        self.digital_pin11_input = 0
        self.digital_pin12_input = 0
        self.digital_pin13_input = 0

        self.digital_pin0_output = 0
        self.digital_pin1_output = 0
        self.digital_pin2_output = 0
        self.digital_pin3_output = 0
        self.digital_pin4_output = 0
        self.digital_pin5_output = 0
        self.digital_pin6_output = 0
        self.digital_pin7_output = 0
        self.digital_pin8_output = 0
        self.digital_pin9_output = 0
        self.digital_pin10_output = 0
        self.digital_pin11_output = 0
        self.digital_pin12_output = 0
        self.digital_pin13_output = 0

        global TkObject_ref
        TkObject_ref = TkObject

        # Load company image
        Imageloc = tk.PhotoImage(file='./Images/alstom_logo.gif')
        label3 = Label(image=Imageloc, )
        label3.image = Imageloc
        label3.place(x=400, y=15)

        # Digital bits header
        dig_pin_status_label = Label(TkObject_ref, text="ARDUINO BOARD DIGITAL PIN STATUS: ",
                                     background="#b7bbc7")
        dig_pin_status_label.place(x=30, y=85)
        dig_pin_status_label.config(font=('helvetica', 15, 'bold'))

        # DIGITAL PIN0
        self.dig_pin0_label = Label(TkObject_ref, text="DIGITAL Pin #0 : ", background="#b7bbc7")
        self.dig_pin0_label.place(x=50, y=130)
        self.dig_pin0_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin0_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin0, value=1, command=self.writeToBoard)
        self.dig_pin0_radio_status.place(x=200, y=130)

        self.dig_pin0_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin0, value=0, command=self.writeToBoard)
        self.dig_pin0_radio_off_status.place(x=250, y=130)

        # DIGITAL PIN1
        self.dig_pin1_label = Label(TkObject_ref, text="DIGITAL Pin #1 : ", background="#b7bbc7")
        self.dig_pin1_label.place(x=50, y=160)
        self.dig_pin1_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin1_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin1, value=1, command=self.writeToBoard)
        self.dig_pin1_radio_status.place(x=200, y=160)

        self.dig_pin1_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin1, value=0, command=self.writeToBoard)
        self.dig_pin1_radio_off_status.place(x=250, y=160)

        # DIGITAL PIN2
        self.dig_pin2_label = Label(TkObject_ref, text="DIGITAL Pin #2 : ", background="#b7bbc7")
        self.dig_pin2_label.place(x=50, y=190)
        self.dig_pin2_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin2_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin2, value=1, command=self.writeToBoard)
        self.dig_pin2_radio_status.place(x=200, y=190)

        self.dig_pin2_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin2, value=0, command=self.writeToBoard)
        self.dig_pin2_radio_off_status.place(x=250, y=190)

        # DIGITAL PIN3
        self.dig_pin3_label = Label(TkObject_ref, text="DIGITAL Pin #3 : ", background="#b7bbc7")
        self.dig_pin3_label.place(x=50, y=220)
        self.dig_pin3_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin3_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin3, value=1, command=self.writeToBoard)
        self.dig_pin3_radio_status.place(x=200, y=220)

        self.dig_pin3_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin3, value=0, command=self.writeToBoard)
        self.dig_pin3_radio_off_status.place(x=250, y=220)

        # DIGITAL PIN4
        self.dig_pin4_label = Label(TkObject_ref, text="DIGITAL Pin #4 : ", background="#b7bbc7")
        self.dig_pin4_label.place(x=50, y=250)
        self.dig_pin4_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin4_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin4, value=1, command=self.writeToBoard)
        self.dig_pin4_radio_status.place(x=200, y=250)

        self.dig_pin4_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin4, value=0, command=self.writeToBoard)
        self.dig_pin4_radio_off_status.place(x=250, y=250)

        # DIGITAL PIN5
        self.dig_pin5_label = Label(TkObject_ref, text="DIGITAL Pin #5 : ", background="#b7bbc7")
        self.dig_pin5_label.place(x=50, y=280)
        self.dig_pin5_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin5_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin5, value=1, command=self.writeToBoard)
        self.dig_pin5_radio_status.place(x=200, y=280)

        self.dig_pin5_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin5, value=0, command=self.writeToBoard)
        self.dig_pin5_radio_off_status.place(x=250, y=280)

        # DIGITAL PIN6
        self.dig_pin6_label = Label(TkObject_ref, text="DIGITAL Pin #6 : ", background="#b7bbc7")
        self.dig_pin6_label.place(x=50, y=310)
        self.dig_pin6_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin6_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin6, value=1, command=self.writeToBoard)
        self.dig_pin6_radio_status.place(x=200, y=310)

        self.dig_pin6_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin6, value=0, command=self.writeToBoard)
        self.dig_pin6_radio_off_status.place(x=250, y=310)

        # DIGITAL PIN7
        self.dig_pin7_label = Label(TkObject_ref, text="DIGITAL Pin #7 : ", background="#b7bbc7")
        self.dig_pin7_label.place(x=50, y=340)
        self.dig_pin7_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin7_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin7, value=1, command=self.writeToBoard)
        self.dig_pin7_radio_status.place(x=200, y=340)

        self.dig_pin7_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin7, value=0, command=self.writeToBoard)
        self.dig_pin7_radio_off_status.place(x=250, y=340)

        # DIGITAL PIN8
        self.dig_pin8_label = Label(TkObject_ref, text="DIGITAL Pin #8 : ", background="#b7bbc7")
        self.dig_pin8_label.place(x=50, y=370)
        self.dig_pin8_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin8_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin8, value=1, command=self.writeToBoard)
        self.dig_pin8_radio_status.place(x=200, y=370)

        self.dig_pin8_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin8, value=0, command=self.writeToBoard)
        self.dig_pin8_radio_off_status.place(x=250, y=370)

        # DIGITAL PIN9
        self.dig_pin9_label = Label(TkObject_ref, text="DIGITAL Pin #9 : ", background="#b7bbc7")
        self.dig_pin9_label.place(x=50, y=400)
        self.dig_pin9_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin9_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin9, value=1, command=self.writeToBoard)
        self.dig_pin9_radio_status.place(x=200, y=400)

        self.dig_pin9_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin9, value=0, command=self.writeToBoard)
        self.dig_pin9_radio_off_status.place(x=250, y=400)

        # DIGITAL PIN10
        self.dig_pin10_label = Label(TkObject_ref, text="DIGITAL Pin #10 : ", background="#b7bbc7")
        self.dig_pin10_label.place(x=50, y=430)
        self.dig_pin10_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin10_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin10, value=1, command=self.writeToBoard)
        self.dig_pin10_radio_status.place(x=200, y=430)

        self.dig_pin10_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin10, value=0, command=self.writeToBoard)
        self.dig_pin10_radio_off_status.place(x=250, y=430)

        # DIGITAL PIN11
        self.dig_pin11_label = Label(TkObject_ref, text="DIGITAL Pin #11 : ", background="#b7bbc7")
        self.dig_pin11_label.place(x=50, y=460)
        self.dig_pin11_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin11_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin11, value=1, command=self.writeToBoard)
        self.dig_pin11_radio_status.place(x=200, y=460)

        self.dig_pin11_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin11, value=0, command=self.writeToBoard)
        self.dig_pin11_radio_off_status.place(x=250, y=460)

        # DIGITAL PIN12
        self.dig_pin12_label = Label(TkObject_ref, text="DIGITAL Pin #12 : ", background="#b7bbc7")
        self.dig_pin12_label.place(x=50, y=490)
        self.dig_pin12_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin12_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin12, value=1, command=self.writeToBoard)
        self.dig_pin12_radio_status.place(x=200, y=490)

        self.dig_pin12_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin12, value=0, command=self.writeToBoard)
        self.dig_pin12_radio_off_status.place(x=250, y=490)

        # DIGITAL PIN13
        self.dig_pin13_label = Label(TkObject_ref, text="DIGITAL Pin #13 : ", background="#b7bbc7")
        self.dig_pin13_label.place(x=50, y=520)
        self.dig_pin13_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin13_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin13, value=1, command=self.writeToBoard)
        self.dig_pin13_radio_status.place(x=200, y=520)

        self.dig_pin13_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin13, value=0, command=self.writeToBoard)
        self.dig_pin13_radio_off_status.place(x=250, y=520)

        syncArdinoDigiPinsWithGUI = Button(TkObject_ref, activebackground='green', borderwidth=4, text='Sync with Arnunio board',
                             command=self.syncWithAurdino)
        syncArdinoDigiPinsWithGUI.place(x=850, y=50)
        syncArdinoDigiPinsWithGUI.config(font=('helvetica', 11, 'bold'))

        # Exit Window
        closeButton = Button(TkObject_ref, activebackground='green', borderwidth=4, text='Close Window',
                             command=self.exitWindow)
        closeButton.place(x=1100, y=50)
        closeButton.config(font=('helvetica', 11, 'bold'))

    def exitWindow(self):
        TkObject_ref.destroy()
        return

    def setDigBitColor(self, digBit_status, prev_digBit_status, radiobuttonOn, radiobuttonOff, val, setBit):

        if setBit is True:
            digBit_status.set(val)
            prev_digBit_status.set(val)

        if val == 1:
            radiobuttonOn.config(fg="green")
            radiobuttonOff.config(fg="black")
        else:
            radiobuttonOff.config(fg="red")
            radiobuttonOn.config(fg="black")

    #This function reads board pins objects once on starting of program
    def initBoardPins(self):

        board = pyfirmata.Arduino('COM3')  # Pass additional parameter to pass port as an argument

        it = pyfirmata.util.Iterator(board)
        it.start()

        self.digital_pin0_input = board.get_pin('d:0:i')
        self.digital_pin1_input = board.get_pin('d:1:i')
        self.digital_pin2_input = board.get_pin('d:2:i')
        self.digital_pin3_input = board.get_pin('d:3:i')
        self.digital_pin4_input = board.get_pin('d:4:i')
        self.digital_pin5_input = board.get_pin('d:5:i')
        self.digital_pin6_input = board.get_pin('d:6:i')
        self.digital_pin7_input = board.get_pin('d:7:i')
        self.digital_pin8_input = board.get_pin('d:8:i')
        self.digital_pin9_input = board.get_pin('d:9:i')
        self.digital_pin10_input = board.get_pin('d:10:i')
        self.digital_pin11_input = board.get_pin('d:11:i')
        self.digital_pin12_input = board.get_pin('d:12:i')
        self.digital_pin13_input = board.get_pin('d:13:i')

        # Initialise Digital bits to default values from board
        self.setDigBitColor(self.dig_pin0, self.dig_pin0_prev_status, self.dig_pin0_radio_status,
                            self.dig_pin0_radio_off_status, int(self.digital_pin0_input.read()), True)
        self.setDigBitColor(self.dig_pin1, self.dig_pin1_prev_status, self.dig_pin1_radio_status,
                            self.dig_pin1_radio_off_status, int(self.digital_pin1_input.read()), True)
        self.setDigBitColor(self.dig_pin2, self.dig_pin2_prev_status, self.dig_pin2_radio_status,
                            self.dig_pin2_radio_off_status, int(self.digital_pin2_input.read()), True)
        self.setDigBitColor(self.dig_pin3, self.dig_pin3_prev_status, self.dig_pin3_radio_status,
                            self.dig_pin3_radio_off_status, int(self.digital_pin3_input.read()), True)
        self.setDigBitColor(self.dig_pin4, self.dig_pin4_prev_status, self.dig_pin4_radio_status,
                            self.dig_pin4_radio_off_status, int(self.digital_pin4_input.read()), True)
        self.setDigBitColor(self.dig_pin5, self.dig_pin5_prev_status, self.dig_pin5_radio_status,
                            self.dig_pin5_radio_off_status, int(self.digital_pin5_input.read()), True)
        self.setDigBitColor(self.dig_pin6, self.dig_pin6_prev_status, self.dig_pin6_radio_status,
                            self.dig_pin6_radio_off_status, int(self.digital_pin6_input.read()), True)
        self.setDigBitColor(self.dig_pin7, self.dig_pin7_prev_status, self.dig_pin7_radio_status,
                            self.dig_pin7_radio_off_status, int(self.digital_pin7_input.read()), True)
        self.setDigBitColor(self.dig_pin8, self.dig_pin8_prev_status, self.dig_pin8_radio_status,
                            self.dig_pin8_radio_off_status, int(self.digital_pin8_input.read()), True)
        self.setDigBitColor(self.dig_pin9, self.dig_pin9_prev_status, self.dig_pin9_radio_status,
                            self.dig_pin9_radio_off_status, int(self.digital_pin9_input.read()), True)
        self.setDigBitColor(self.dig_pin10, self.dig_pin10_prev_status, self.dig_pin10_radio_status,
                            self.dig_pin10_radio_off_status, int(self.digital_pin10_input.read()), True)
        self.setDigBitColor(self.dig_pin11, self.dig_pin11_prev_status, self.dig_pin11_radio_status,
                            self.dig_pin11_radio_off_status, int(self.digital_pin11_input.read()), True)
        self.setDigBitColor(self.dig_pin12, self.dig_pin12_prev_status, self.dig_pin12_radio_status,
                            self.dig_pin12_radio_off_status, int(self.digital_pin12_input.read()), True)
        self.setDigBitColor(self.dig_pin13, self.dig_pin13_prev_status, self.dig_pin13_radio_status,
                            self.dig_pin13_radio_off_status, int(self.digital_pin13_input.read()), True)

        self.digital_pin0_output = board.get_pin('d:0:o')
        self.digital_pin1_output = board.get_pin('d:1:o')
        self.digital_pin2_output = board.get_pin('d:2:o')
        self.digital_pin3_output = board.get_pin('d:3:o')
        self.digital_pin4_output = board.get_pin('d:4:o')
        self.digital_pin5_output = board.get_pin('d:5:o')
        self.digital_pin6_output = board.get_pin('d:6:o')
        self.digital_pin7_output = board.get_pin('d:7:o')
        self.digital_pin8_output = board.get_pin('d:8:o')
        self.digital_pin9_output = board.get_pin('d:9:o')
        self.digital_pin10_output = board.get_pin('d:10:o')
        self.digital_pin11_output = board.get_pin('d:11:o')
        self.digital_pin12_output = board.get_pin('d:12:o')
        self.digital_pin13_output = board.get_pin('d:13:o')

    def keepReadingDigiBitsForEver(self):

            # Iteratively keep reading digi bits from board and set corrosponding bits on GUI if there a change
            #while True:

            if self.dig_pin0_prev_status != int(self.digital_pin0_input.read()):
                self.setDigBitColor(self.dig_pin0, self.dig_pin0_prev_status, self.dig_pin0_radio_status,
                                    self.dig_pin0_radio_off_status, int(self.digital_pin0_input.read()), True)

            if self.dig_pin1_prev_status != int(self.digital_pin1_input.read()):
                self.setDigBitColor(self.dig_pin1, self.dig_pin1_prev_status, self.dig_pin1_radio_status,
                                    self.dig_pin1_radio_off_status, int(self.digital_pin1_input.read()), True)

            if self.dig_pin2_prev_status != int(self.digital_pin2_input.read()):
                self.setDigBitColor(self.dig_pin2, self.dig_pin2_prev_status, self.dig_pin2_radio_status,
                                    self.dig_pin2_radio_off_status, int(self.digital_pin2_input.read()), True)

            if self.dig_pin3_prev_status != int(self.digital_pin3_input.read()):
                self.setDigBitColor(self.dig_pin3, self.dig_pin3_prev_status, self.dig_pin3_radio_status,
                                    self.dig_pin3_radio_off_status, int(self.digital_pin3_input.read()), True)

            if self.dig_pin4_prev_status != int(self.digital_pin4_input.read()):
                self.setDigBitColor(self.dig_pin4, self.dig_pin4_prev_status, self.dig_pin4_radio_status,
                                    self.dig_pin4_radio_off_status, int(self.digital_pin4_input.read()), True)

            if self.dig_pin5_prev_status != int(self.digital_pin5_input.read()):
                self.setDigBitColor(self.dig_pin5, self.dig_pin5_prev_status, self.dig_pin5_radio_status,
                                    self.dig_pin5_radio_off_status, int(self.digital_pin5_input.read()), True)

            if self.dig_pin6_prev_status != int(self.digital_pin6_input.read()):
                self.setDigBitColor(self.dig_pin6, self.dig_pin6_prev_status, self.dig_pin6_radio_status,
                                    self.dig_pin6_radio_off_status, int(self.digital_pin6_input.read()), True)

            if self.dig_pin7_prev_status != int(self.digital_pin7_input.read()):
                self.setDigBitColor(self.dig_pin7, self.dig_pin7_prev_status, self.dig_pin7_radio_status,
                                    self.dig_pin7_radio_off_status, int(self.digital_pin7_input.read()), True)

            if self.dig_pin8_prev_status != int(self.digital_pin8_input.read()):
                self.setDigBitColor(self.dig_pin8, self.dig_pin8_prev_status, self.dig_pin8_radio_status,
                                    self.dig_pin8_radio_off_status, int(self.digital_pin8_input.read()), True)

            if self.dig_pin9_prev_status != int(self.digital_pin9_input.read()):
                self.setDigBitColor(self.dig_pin9, self.dig_pin9_prev_status, self.dig_pin9_radio_status,
                                    self.dig_pin9_radio_off_status, int(self.digital_pin9_input.read()), True)

            if self.dig_pin10_prev_status != int(self.digital_pin10_input.read()):
                self.setDigBitColor(self.dig_pin10, self.dig_pin10_prev_status, self.dig_pin10_radio_status,
                                    self.dig_pin10_radio_off_status, int(self.digital_pin10_input.read()), True)

            if self.dig_pin11_prev_status != int(self.digital_pin11_input.read()):
                self.setDigBitColor(self.dig_pin11, self.dig_pin11_prev_status, self.dig_pin11_radio_status,
                                    self.dig_pin11_radio_off_status, int(self.digital_pin11_input.read()), True)

            if self.dig_pin12_prev_status != int(self.digital_pin12_input.read()):
                self.setDigBitColor(self.dig_pin12, self.dig_pin12_prev_status, self.dig_pin12_radio_status,
                                    self.dig_pin12_radio_off_status, int(self.digital_pin12_input.read()), True)

            if self.dig_pin13_prev_status != int(self.digital_pin13_input.read()):
                self.setDigBitColor(self.dig_pin13, self.dig_pin13_prev_status, self.dig_pin13_radio_status,
                                    self.dig_pin13_radio_off_status, int(self.digital_pin13_input.read()), True)

    def syncWithAurdino(self):

        try:

            if self.syncWithBoardOnce is False:
                self.syncWithBoardOnce = True
                self.initBoardPins()

            self.keepReadingDigiBitsForEver()

        except Exception as e:
            messagebox.showerror('Error', e) #Display error message if anything occures
            sys.exit(0)

    def writeToBoard(self):

        try:
            if (self.dig_pin0.get() != self.dig_pin0_prev_status.get()):
                self.dig_pin0_prev_status.set(self.dig_pin0.get())
                self.digital_pin0_output.write(int(self.dig_pin0.get()))
                self.setDigBitColor(None, None, self.dig_pin0_radio_status,  self.dig_pin0_radio_off_status, self.dig_pin0.get(), False)

            if (self.dig_pin1.get() != self.dig_pin1_prev_status.get()):
                self.dig_pin1_prev_status.set(self.dig_pin1.get())
                self.digital_pin1_output.write(int(self.dig_pin1.get()))
                self.setDigBitColor(self.dig_pin1_radio_status,  self.dig_pin1_radio_off_status,self.dig_pin1.get())

            if (self.dig_pin2.get() != self.dig_pin2_prev_status.get()):
                self.dig_pin2_prev_status.set(self.dig_pin2.get())
                self.digital_pin2_output.write(int(self.dig_pin2.get()))
                self.setDigBitColor(self.dig_pin2_radio_status,  self.dig_pin2_radio_off_status,self.dig_pin2.get())

            if (self.dig_pin3.get() != self.dig_pin3_prev_status.get()):
                self.dig_pin3_prev_status.set(self.dig_pin3.get())
                self.digital_pin3_output.write(int(self.dig_pin3.get()))
                self.setDigBitColor(self.dig_pin3_radio_status,  self.dig_pin3_radio_off_status,self.dig_pin3.get())

            if (self.dig_pin4.get() != self.dig_pin4_prev_status.get()):
                self.dig_pin4_prev_status.set(self.dig_pin4.get())
                self.digital_pin4_output.write(int(self.dig_pin4.get()))
                self.setDigBitColor(self.dig_pin4_radio_status,  self.dig_pin4_radio_off_status,self.dig_pin4.get())

            if (self.dig_pin5.get() != self.dig_pin5_prev_status.get()):
                self.dig_pin5_prev_status.set(self.dig_pin5.get())
                self.digital_pin5_output.write(int(self.dig_pin5.get()))
                self.setDigBitColor(self.dig_pin5_radio_status,  self.dig_pin5_radio_off_status,self.dig_pin5.get())

            if (self.dig_pin6.get() != self.dig_pin6_prev_status.get()):
                self.dig_pin6_prev_status.set(self.dig_pin6.get())
                self.digital_pin6_output.write(int(self.dig_pin6.get()))
                self.setDigBitColor(self.dig_pin6_radio_status,  self.dig_pin6_radio_off_status,self.dig_pin6.get())

            if (self.dig_pin7.get() != self.dig_pin7_prev_status.get()):
                self.dig_pin7_prev_status.set(self.dig_pin7.get())
                self.digital_pin7_output.write(int(self.dig_pin7.get()))
                self.setDigBitColor(self.dig_pin7_radio_status,  self.dig_pin7_radio_off_status,self.dig_pin7.get())

            if (self.dig_pin8.get() != self.dig_pin8_prev_status.get()):
                self.dig_pin8_prev_status.set(self.dig_pin8.get())
                self.digital_pin8_output.write(int(self.dig_pin8.get()))
                self.setDigBitColor(self.dig_pin8_radio_status,  self.dig_pin8_radio_off_status,self.dig_pin8.get())

            if (self.dig_pin9.get() != self.dig_pin9_prev_status.get()):
                self.dig_pin9_prev_status.set(self.dig_pin9.get())
                self.digital_pin9_output.write(int(self.dig_pin9.get()))
                self.setDigBitColor(self.dig_pin9_radio_status,  self.dig_pin9_radio_off_status,self.dig_pin9.get())

            if (self.dig_pin10.get() != self.dig_pin10_prev_status.get()):
                self.dig_pin10_prev_status.set(self.dig_pin10.get())
                self.digital_pin10_output.write(int(self.dig_pin10.get()))
                self.setDigBitColor(self.dig_pin10_radio_status,  self.dig_pin10_radio_off_status,self.dig_pin10.get())

            if (self.dig_pin11.get() != self.dig_pin11_prev_status.get()):
                self.dig_pin11_prev_status.set(self.dig_pin11.get())
                self.digital_pin11_output.write(int(self.dig_pin11.get()))
                self.setDigBitColor(self.dig_pin11_radio_status,  self.dig_pin11_radio_off_status,self.dig_pin11.get())

            if (self.dig_pin12.get() != self.dig_pin12_prev_status.get()):
                self.dig_pin12_prev_status.set(self.dig_pin12.get())
                self.digital_pin12_output.write(int(self.dig_pin12.get()))
                self.setDigBitColor(self.dig_pin12_radio_status,  self.dig_pin12_radio_off_status,self.dig_pin12.get())

            if (self.dig_pin13.get() != self.dig_pin13_prev_status.get()):
                self.dig_pin13_prev_status.set(self.dig_pin13.get())
                self.digital_pin13_output.write(int(self.dig_pin13.get()))
                self.setDigBitColor(self.dig_pin13_radio_status,  self.dig_pin13_radio_off_status,self.dig_pin13.get())

        except Exception as e:
            messagebox.showerror("Error", "Please press \"Sync with Arduino\" button first if you have missed.\n\n"+str(e))

if __name__ == '__main__':
    root = tk.Tk()

    # Change the background window color
    root.configure(background='#b7bbc7')
    root.state('zoomed')

    # Set window parameters
    root.geometry('850x620')
    root.title('Arduino Board Control Operations')

    # Removes the maximizing option
    #root.resizable(0, 0)

    ObjController = GUI_COntroller(root)

    # keep the main window is running
    root.mainloop()
    sys.exit()
