#https://realpython.com/arduino-python/
#https://github.com/tino/pyFirmata#usage

from tkinter import Label, Button, Radiobutton, messagebox, Checkbutton, DISABLED, OptionMenu, BOTTOM, X, SUNKEN, W, Entry

import tkinter as tk
import sys, pyfirmata, threading, time, os
import serial.tools.list_ports

class GUI_COntroller(tk.Frame):
    '''
	   This class initialize the required controls for TkInter GUI
	'''

    def __init__(self, TkObject):

        tk.Frame.__init__(self,TkObject)

        self.syncWithBoardOnce = False
        self.selectedCommPort = tk.StringVar()
        self.initSuccess = False
        self.statusBarText = tk.StringVar()

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

        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()

        self.syncArdinoDigiPinsWithGUI = None

        self.analog_pin0_reading = None
        self.analog_pin1_reading = None
        self.analog_pin2_reading = None
        self.analog_pin3_reading = None
        self.analog_pin4_reading = None
        self.analog_pin5_reading = None

        self.analog_pin0_input = None
        self.analog_pin1_input = None
        self.analog_pin2_input = None
        self.analog_pin3_input = None
        self.analog_pin4_input = None
        self.analog_pin5_input = None

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
        self.allDigONButton = None
        self.allDigOFFButton = None

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
        Imageloc = tk.PhotoImage(file='../Images/alstom_logo.gif')
        label3 = Label(image=Imageloc, )
        label3.image = Imageloc
        label3.place(x=400, y=15)

        # Digital bits header
        dig_pin_status_label = Label(TkObject_ref, text="ARDUINO BOARD DIGITAL and ANALOG PIN STATUS: ",
                                     background="orange")
        dig_pin_status_label.place(x=300, y=85)
        dig_pin_status_label.config(font=('helvetica', 15, 'bold'))

        # DIGITAL PIN0
        # self.dig_pin0_label = Label(TkObject_ref, text="DIGITAL Pin #0 : ", background="#b7bbc7")
        # self.dig_pin0_label.place(x=50, y=130)
        # self.dig_pin0_label.config(font=('helvetica', 10, 'bold'), state = DISABLED)

        # self.dig_pin0_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin0, value=1, command=self.writeToBoard)
        # self.dig_pin0_radio_status.place(x=200, y=130)

        # self.dig_pin0_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin0, value=0, command=self.writeToBoard)
        # self.dig_pin0_radio_off_status.place(x=250, y=130)

        # DIGITAL PIN1
        # self.dig_pin1_label = Label(TkObject_ref, text="DIGITAL Pin #1 : ", background="#b7bbc7")
        # self.dig_pin1_label.place(x=50, y=160)
        # self.dig_pin1_label.config(font=('helvetica', 10, 'bold'), state = DISABLED)

        # self.dig_pin1_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin1, value=1, command=self.writeToBoard)
        # self.dig_pin1_radio_status.place(x=200, y=160)

        # self.dig_pin1_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin1, value=0, command=self.writeToBoard)
        # self.dig_pin1_radio_off_status.place(x=250, y=160)

        # DIGITAL PIN2
        self.dig_pin2_label = Label(TkObject_ref, text="DIGITAL Pin #1 : ", background="#b7bbc7")
        self.dig_pin2_label.place(x=50, y=150)
        self.dig_pin2_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin2_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin2, value=1, command=self.writeToBoard)
        self.dig_pin2_radio_status.place(x=200, y=150)

        self.dig_pin2_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin2, value=0, command=self.writeToBoard)
        self.dig_pin2_radio_off_status.place(x=250, y=150)

        # DIGITAL PIN3
        self.dig_pin3_label = Label(TkObject_ref, text="DIGITAL Pin #2 : ", background="#b7bbc7")
        self.dig_pin3_label.place(x=50, y=180)
        self.dig_pin3_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin3_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin3, value=1, command=self.writeToBoard)
        self.dig_pin3_radio_status.place(x=200, y=180)

        self.dig_pin3_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin3, value=0, command=self.writeToBoard)
        self.dig_pin3_radio_off_status.place(x=250, y=180)

        # DIGITAL PIN4
        self.dig_pin4_label = Label(TkObject_ref, text="DIGITAL Pin #3 : ", background="#b7bbc7")
        self.dig_pin4_label.place(x=50, y=210)
        self.dig_pin4_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin4_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin4, value=1, command=self.writeToBoard)
        self.dig_pin4_radio_status.place(x=200, y=210)

        self.dig_pin4_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin4, value=0, command=self.writeToBoard)
        self.dig_pin4_radio_off_status.place(x=250, y=210)

        # DIGITAL PIN5
        self.dig_pin5_label = Label(TkObject_ref, text="DIGITAL Pin #4 : ", background="#b7bbc7")
        self.dig_pin5_label.place(x=50, y=240)
        self.dig_pin5_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin5_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin5, value=1, command=self.writeToBoard)
        self.dig_pin5_radio_status.place(x=200, y=240)

        self.dig_pin5_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin5, value=0, command=self.writeToBoard)
        self.dig_pin5_radio_off_status.place(x=250, y=240)

        # DIGITAL PIN6
        self.dig_pin6_label = Label(TkObject_ref, text="DIGITAL Pin #5 : ", background="#b7bbc7")
        self.dig_pin6_label.place(x=50, y=270)
        self.dig_pin6_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin6_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin6, value=1, command=self.writeToBoard)
        self.dig_pin6_radio_status.place(x=200, y=270)

        self.dig_pin6_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin6, value=0, command=self.writeToBoard)
        self.dig_pin6_radio_off_status.place(x=250, y=270)

        # DIGITAL PIN7
        self.dig_pin7_label = Label(TkObject_ref, text="DIGITAL Pin #6 : ", background="#b7bbc7")
        self.dig_pin7_label.place(x=50, y=300)
        self.dig_pin7_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin7_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin7, value=1, command=self.writeToBoard)
        self.dig_pin7_radio_status.place(x=200, y=300)

        self.dig_pin7_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin7, value=0, command=self.writeToBoard)
        self.dig_pin7_radio_off_status.place(x=250, y=300)

        # DIGITAL PIN8
        self.dig_pin8_label = Label(TkObject_ref, text="DIGITAL Pin #7 : ", background="#b7bbc7")
        self.dig_pin8_label.place(x=50, y=330)
        self.dig_pin8_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin8_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin8, value=1, command=self.writeToBoard)
        self.dig_pin8_radio_status.place(x=200, y=330)

        self.dig_pin8_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin8, value=0, command=self.writeToBoard)
        self.dig_pin8_radio_off_status.place(x=250, y=330)

        # DIGITAL PIN9
        self.dig_pin9_label = Label(TkObject_ref, text="DIGITAL Pin #8 : ", background="#b7bbc7")
        self.dig_pin9_label.place(x=50, y=360)
        self.dig_pin9_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin9_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin9, value=1, command=self.writeToBoard)
        self.dig_pin9_radio_status.place(x=200, y=360)

        self.dig_pin9_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin9, value=0, command=self.writeToBoard)
        self.dig_pin9_radio_off_status.place(x=250, y=360)

        # DIGITAL PIN10
        self.dig_pin10_label = Label(TkObject_ref, text="DIGITAL Pin #9 : ", background="#b7bbc7")
        self.dig_pin10_label.place(x=50, y=390)
        self.dig_pin10_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin10_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin10, value=1, command=self.writeToBoard)
        self.dig_pin10_radio_status.place(x=200, y=390)

        self.dig_pin10_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin10, value=0, command=self.writeToBoard)
        self.dig_pin10_radio_off_status.place(x=250, y=390)

        # DIGITAL PIN11
        self.dig_pin11_label = Label(TkObject_ref, text="DIGITAL Pin #10 : ", background="#b7bbc7")
        self.dig_pin11_label.place(x=50, y=420)
        self.dig_pin11_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin11_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin11, value=1, command=self.writeToBoard)
        self.dig_pin11_radio_status.place(x=200, y=420)

        self.dig_pin11_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin11, value=0, command=self.writeToBoard)
        self.dig_pin11_radio_off_status.place(x=250, y=420)

        # DIGITAL PIN12
        self.dig_pin12_label = Label(TkObject_ref, text="DIGITAL Pin #11 : ", background="#b7bbc7")
        self.dig_pin12_label.place(x=50, y=450)
        self.dig_pin12_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin12_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin12, value=1, command=self.writeToBoard)
        self.dig_pin12_radio_status.place(x=200, y=450)

        self.dig_pin12_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin12, value=0, command=self.writeToBoard)
        self.dig_pin12_radio_off_status.place(x=250, y=450)

        # DIGITAL PIN13
        self.dig_pin13_label = Label(TkObject_ref, text="DIGITAL Pin #12 : ", background="#b7bbc7")
        self.dig_pin13_label.place(x=50, y=480)
        self.dig_pin13_label.config(font=('helvetica', 10, 'bold'))

        self.dig_pin13_radio_status = Radiobutton(TkObject_ref, text="ON", background="#b7bbc7", variable=self.dig_pin13, value=1, command=self.writeToBoard)
        self.dig_pin13_radio_status.place(x=200, y=480)

        self.dig_pin13_radio_off_status = Radiobutton(TkObject_ref, text="OFF", background="#b7bbc7", variable=self.dig_pin13, value=0, command=self.writeToBoard)
        self.dig_pin13_radio_off_status.place(x=250, y=480)

        self.syncArdinoDigiPinsWithGUI = Button(TkObject_ref, activebackground='red', background='red', borderwidth=4, height=5, text='CLICK HERE TO SYNC WITH ARDUINO BOARD',
                             command=self.syncWithAurdino)
        self.syncArdinoDigiPinsWithGUI.place(x=880, y=200)
        self.syncArdinoDigiPinsWithGUI.config(font=('helvetica', 11, 'bold'))

        # DIGITAL PIN13
        self.digiTurnON = Label(TkObject_ref, text="TURN ON: ", background="#b7bbc7")
        self.digiTurnON.place(x=50, y=540)
        self.digiTurnON.config(font=('helvetica', 12, 'bold'))

        # Set all Dig Pin ON
        self.allDigONButton = Checkbutton(TkObject_ref, activebackground='green', borderwidth=2, text='ALL',
                             command=self.allDigON, variable=self.CheckVar1)
        self.allDigONButton.place(x=190, y=540)
        self.allDigONButton.config(font=('helvetica', 9, 'bold'), state=DISABLED)

        # Set all Dig Pin OFF
        self.allDigOFFButton = Checkbutton(TkObject_ref, activebackground='green', borderwidth=2, text='NONE',
                             command=self.allDigOFF, variable=self.CheckVar2)
        self.allDigOFFButton.place(x=250, y=540)
        self.allDigOFFButton.config(font=('helvetica', 9, 'bold'), state=DISABLED)

        # Exit Window
        closeButton = Button(TkObject_ref, activebackground='green', borderwidth=4, text='Close Window',
                             command=self.exitWindow)
        closeButton.place(x=1000, y=30)
        closeButton.config(font=('helvetica', 11, 'bold'))

        StatusLabel = Label(TkObject_ref, textvariable=self.statusBarText, fg="green", bd=1,relief=SUNKEN,anchor=W)
        StatusLabel.config(font=('helvetica',11,'bold'))
        StatusLabel.pack(side=BOTTOM, fill=X)

        self.analogDesignOnUI()

        #Disable Dig 0 and 1 bits as they used for Tx and Rx
        #self.disabledDigBit0Bit1()

        # ConfigureListBox
        self.configureListoxForSerialPort()

    def analogDesignOnUI(self):
        # DIGITAL PIN0
        analog_pin0_label = Label(TkObject_ref, text="Analog Pin #0 : ", background="#b7bbc7")
        analog_pin0_label.place(x=400, y=190)
        analog_pin0_label.config(font=('helvetica', 10, 'bold'))

        self.analog_pin0_reading = tk.StringVar()
        analog_pin0_Entry= Entry(TkObject_ref, width=10, textvariable=self.analog_pin0_reading, bd=1)
        analog_pin0_Entry.place(x=520,y=190)
        analog_pin0_Entry.config(font=('helvetica',10), state="readonly")

        analog_pin1_label = Label(TkObject_ref, text="Analog Pin #1 : ", background="#b7bbc7")
        analog_pin1_label.place(x=400, y=220)
        analog_pin1_label.config(font=('helvetica', 10, 'bold'))

        self.analog_pin1_reading = tk.StringVar()
        analog_pin1_Entry= Entry(TkObject_ref, width=10, textvariable=self.analog_pin1_reading, bd=1)
        analog_pin1_Entry.place(x=520,y=220)
        analog_pin1_Entry.config(font=('helvetica',10), state="readonly")

        analog_pin2_label = Label(TkObject_ref, text="Analog Pin #2 : ", background="#b7bbc7")
        analog_pin2_label.place(x=400, y=250)
        analog_pin2_label.config(font=('helvetica', 10, 'bold'))

        self.analog_pin2_reading = tk.StringVar()
        analog_pin2_Entry= Entry(TkObject_ref, width=10, textvariable=self.analog_pin2_reading, bd=1)
        analog_pin2_Entry.place(x=520,y=250)
        analog_pin2_Entry.config(font=('helvetica',10), state="readonly")

        analog_pin3_label = Label(TkObject_ref, text="Analog Pin #3 : ", background="#b7bbc7")
        analog_pin3_label.place(x=400, y=280)
        analog_pin3_label.config(font=('helvetica', 10, 'bold'))

        self.analog_pin3_reading = tk.StringVar()
        analog_pin3_Entry= Entry(TkObject_ref, width=10, textvariable=self.analog_pin3_reading, bd=1)
        analog_pin3_Entry.place(x=520,y=280)
        analog_pin3_Entry.config(font=('helvetica',10), state="readonly")

        analog_pin4_label = Label(TkObject_ref, text="Analog Pin #4 : ", background="#b7bbc7")
        analog_pin4_label.place(x=400, y=310)
        analog_pin4_label.config(font=('helvetica', 10, 'bold'))

        self.analog_pin4_reading = tk.StringVar()
        analog_pin4_Entry= Entry(TkObject_ref, width=10, textvariable=self.analog_pin4_reading, bd=1)
        analog_pin4_Entry.place(x=520,y=310)
        analog_pin4_Entry.config(font=('helvetica',10), state="readonly")

        analog_pin5_label = Label(TkObject_ref, text="Analog Pin #5 : ", background="#b7bbc7")
        analog_pin5_label.place(x=400, y=340)
        analog_pin5_label.config(font=('helvetica', 10, 'bold'))

        self.analog_pin5_reading = tk.StringVar()
        analog_pin5_Entry= Entry(TkObject_ref, width=10, textvariable=self.analog_pin5_reading, bd=1)
        analog_pin5_Entry.place(x=520,y=340)
        analog_pin5_Entry.config(font=('helvetica',10), state="readonly")


    def configureListoxForSerialPort(self):

        try:
            global TkObject_ref
            self.dig_pin13_label = Label(TkObject_ref, text="Select Serial Port : ", background="#b7bbc7")
            self.dig_pin13_label.place(x=780, y=350)
            self.dig_pin13_label.config(font=('helvetica', 10, 'bold'))

            comPorts = list(serial.tools.list_ports.comports())
            if len(comPorts) > 0:
                comPorts.insert(0,"-- Select Arduino Board connected Serial Port --")
                self.selectedCommPort.set(comPorts[0])
            else:
                comPorts.append("-- No Serial ports connected --")
                self.selectedCommPort.set(comPorts[0])

            #Select Comm port
            selectSerialPortMenu = OptionMenu(TkObject_ref, self.selectedCommPort, *comPorts)
            selectSerialPortMenu.config(width=40)
            selectSerialPortMenu.place(x=930, y=345)

        except Exception as e:
            messagebox.showerror("Error","Something went wrong while selecting serial port from options\n"+str(e))
            sys.exit()

    def disabledDigBit0Bit1(self):
        self.dig_pin0_radio_status.config(state = DISABLED)
        self.dig_pin0_radio_off_status.config(state = DISABLED)
        self.dig_pin1_radio_status.config(state = DISABLED)
        self.dig_pin1_radio_off_status.config(state = DISABLED)

    def allDigON(self):
        self.CheckVar2.set(0)
        self.setDigBitColor(self.dig_pin2, self.dig_pin2_prev_status, self.dig_pin2_radio_status, self.dig_pin2_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin3, self.dig_pin3_prev_status, self.dig_pin3_radio_status, self.dig_pin3_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin4, self.dig_pin4_prev_status, self.dig_pin4_radio_status, self.dig_pin4_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin5, self.dig_pin5_prev_status, self.dig_pin5_radio_status, self.dig_pin5_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin6, self.dig_pin6_prev_status, self.dig_pin6_radio_status, self.dig_pin6_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin7, self.dig_pin7_prev_status, self.dig_pin7_radio_status, self.dig_pin7_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin8, self.dig_pin8_prev_status, self.dig_pin8_radio_status, self.dig_pin8_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin9, self.dig_pin9_prev_status, self.dig_pin9_radio_status, self.dig_pin9_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin10, self.dig_pin10_prev_status, self.dig_pin10_radio_status, self.dig_pin10_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin11, self.dig_pin11_prev_status, self.dig_pin11_radio_status, self.dig_pin11_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin12, self.dig_pin12_prev_status, self.dig_pin12_radio_status, self.dig_pin12_radio_off_status, 1, True)
        self.setDigBitColor(self.dig_pin13, self.dig_pin13_prev_status, self.dig_pin13_radio_status, self.dig_pin13_radio_off_status, 1, True)

    def allDigOFF(self):
        self.CheckVar1.set(0)
        self.setDigBitColor(self.dig_pin2, self.dig_pin2_prev_status, self.dig_pin2_radio_status, self.dig_pin2_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin3, self.dig_pin3_prev_status, self.dig_pin3_radio_status, self.dig_pin3_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin4, self.dig_pin4_prev_status, self.dig_pin4_radio_status, self.dig_pin4_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin5, self.dig_pin5_prev_status, self.dig_pin5_radio_status, self.dig_pin5_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin6, self.dig_pin6_prev_status, self.dig_pin6_radio_status, self.dig_pin6_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin7, self.dig_pin7_prev_status, self.dig_pin7_radio_status, self.dig_pin7_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin8, self.dig_pin8_prev_status, self.dig_pin8_radio_status, self.dig_pin8_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin9, self.dig_pin9_prev_status, self.dig_pin9_radio_status, self.dig_pin9_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin10, self.dig_pin10_prev_status, self.dig_pin10_radio_status, self.dig_pin10_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin11, self.dig_pin11_prev_status, self.dig_pin11_radio_status, self.dig_pin11_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin12, self.dig_pin12_prev_status, self.dig_pin12_radio_status, self.dig_pin12_radio_off_status, 0, True)
        self.setDigBitColor(self.dig_pin13, self.dig_pin13_prev_status, self.dig_pin13_radio_status, self.dig_pin13_radio_off_status, 0, True)

    def exitWindow(self):
        TkObject_ref.destroy()
        return

    def pickComPortNum(self,portDetails):

        try:
            port = (portDetails.split("-")[0]).strip()
            return port
        except Exception as e:
            messagebox.showerror("Error","Incorrect format of Port identified, application needs to be modified for this, please contact Masthan")
            sys.exit()

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

    def readAnalogData(self,analogTextBox, val):
        if val is None:
            analogTextBox.set("None")
        else:
            analogTextBox.set(val)

    def digPinStatus(self,Digpin):
        dig_pin = Digpin
        if Digpin is None:
            dig_pin = 0
        return dig_pin

    #This function reads board pins objects once on starting of program
    def initBoardPins(self):

        if self.selectedCommPort.get() in ["-- No Serial ports connected --","-- Select Arduino Board connected Serial Port --"]:
            messagebox.showerror("Error","No Comport selected/identfied for arduino board, please try again")
            self.initSuccess = False
            self.syncWithBoardOnce = False
        elif self.initSuccess is False:
                self.dig_pin2_prev_status.set(0)

                self.statusBarText.set("Please wait syncing with Arduino board...")
                port = self.pickComPortNum(self.selectedCommPort.get())

                board = pyfirmata.Arduino(port)  # Pass additional parameter to pass port as an argument

                it = pyfirmata.util.Iterator(board)
                it.start()

                #self.digital_pin0_output = board.get_pin('d:0:o') #Commented out these pin as it is used for only Tx
                #self.digital_pin1_output = board.get_pin('d:1:o') #Commented out these pin as it is used for only Rx
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

                #Analog Pins
                self.analog_pin0_input = board.get_pin('a:0:i')
                self.analog_pin1_input = board.get_pin('a:1:i')
                self.analog_pin2_input = board.get_pin('a:2:i')
                self.analog_pin3_input = board.get_pin('a:3:i')
                self.analog_pin4_input = board.get_pin('a:4:i')
                self.analog_pin5_input = board.get_pin('a:5:i')

                # Initialise Digital bits to default values from board
                #self.setDigBitColor(self.dig_pin0, self.dig_pin0_prev_status, self.dig_pin0_radio_status,
                #                    self.dig_pin0_radio_off_status, int(self.digital_pin0_input.read()), True)
                #self.setDigBitColor(self.dig_pin1, self.dig_pin1_prev_status, self.dig_pin1_radio_status,
                #                    self.dig_pin1_radio_off_status, int(self.digital_pin1_input.read()), True)

                self.setDigBitColor(self.dig_pin2, self.dig_pin2_prev_status, self.dig_pin2_radio_status,
                                    self.dig_pin2_radio_off_status, self.digPinStatus(self.digital_pin2_output.read()), True)
                self.setDigBitColor(self.dig_pin3, self.dig_pin3_prev_status, self.dig_pin3_radio_status,
                                    self.dig_pin3_radio_off_status, self.digPinStatus(self.digital_pin3_output.read()), True)
                self.setDigBitColor(self.dig_pin4, self.dig_pin4_prev_status, self.dig_pin4_radio_status,
                                    self.dig_pin4_radio_off_status, self.digPinStatus(self.digital_pin4_output.read()), True)
                self.setDigBitColor(self.dig_pin5, self.dig_pin5_prev_status, self.dig_pin5_radio_status,
                                    self.dig_pin5_radio_off_status, self.digPinStatus(self.digital_pin5_output.read()), True)
                self.setDigBitColor(self.dig_pin6, self.dig_pin6_prev_status, self.dig_pin6_radio_status,
                                    self.dig_pin6_radio_off_status, self.digPinStatus(self.digital_pin6_output.read()), True)
                self.setDigBitColor(self.dig_pin7, self.dig_pin7_prev_status, self.dig_pin7_radio_status,
                                    self.dig_pin7_radio_off_status, self.digPinStatus(self.digital_pin7_output.read()), True)
                self.setDigBitColor(self.dig_pin8, self.dig_pin8_prev_status, self.dig_pin8_radio_status,
                                    self.dig_pin8_radio_off_status, self.digPinStatus(self.digital_pin8_output.read()), True)
                self.setDigBitColor(self.dig_pin9, self.dig_pin9_prev_status, self.dig_pin9_radio_status,
                                    self.dig_pin9_radio_off_status, self.digPinStatus(self.digital_pin9_output.read()), True)
                self.setDigBitColor(self.dig_pin10, self.dig_pin10_prev_status, self.dig_pin10_radio_status,
                                    self.dig_pin10_radio_off_status, self.digPinStatus(self.digital_pin10_output.read()), True)
                self.setDigBitColor(self.dig_pin11, self.dig_pin11_prev_status, self.dig_pin11_radio_status,
                                    self.dig_pin11_radio_off_status, self.digPinStatus(self.digital_pin11_output.read()), True)
                self.setDigBitColor(self.dig_pin12, self.dig_pin12_prev_status, self.dig_pin12_radio_status,
                                    self.dig_pin12_radio_off_status, self.digPinStatus(self.digital_pin12_output.read()), True)
                self.setDigBitColor(self.dig_pin13, self.dig_pin13_prev_status, self.dig_pin13_radio_status,
                                    self.dig_pin13_radio_off_status, self.digPinStatus(self.digital_pin13_output.read()), True)

                #read Analog ports
                time.sleep(2)
                self.readAnalogData(self.analog_pin0_reading, self.analog_pin0_input.read())
                self.readAnalogData(self.analog_pin1_reading, self.analog_pin1_input.read())
                self.readAnalogData(self.analog_pin2_reading, self.analog_pin2_input.read())
                self.readAnalogData(self.analog_pin3_reading, self.analog_pin3_input.read())
                #self.readAnalogData(self.analog_pin4_reading, self.analog_pin4_input.read())
                #self.readAnalogData(self.analog_pin5_reading, self.analog_pin5_input.read())

                self.initSuccess = True
                self.syncArdinoDigiPinsWithGUI.config(bg="Green", text="ARDUINO BOARD IN SYNC WITH GUI\n(Click Again to read pins status)")
                self.statusBarText.set("UI synced with Arduino board.")

                self.allDigOFFButton.config(state="normal")
                self.allDigONButton.config(state="normal")

    def keepReadingDigiBitsForEver(self):

            # Iteratively keep reading digi bits from board and set corrosponding bits on GUI if there a change
            #while True:
            # if self.dig_pin0_prev_status != int(self.digital_pin0_output.read()):
            #    self.setDigBitColor(self.dig_pin0, self.dig_pin0_prev_status, self.dig_pin0_radio_status,
            #                        self.dig_pin0_radio_off_status, int(self.digital_pin0_output.read()), True)
            #
            # if self.dig_pin1_prev_status != int(self.digital_pin1_output.read()):
            #    self.setDigBitColor(self.dig_pin1, self.dig_pin1_prev_status, self.dig_pin1_radio_status,
            #                        self.dig_pin1_radio_off_status, int(self.digital_pin1_output.read()), True)

            if self.dig_pin2_prev_status.get() != self.digPinStatus(self.digital_pin2_output.read()):
                self.setDigBitColor(self.dig_pin2, self.dig_pin2_prev_status, self.dig_pin2_radio_status,
                                        self.dig_pin2_radio_off_status, self.digPinStatus(self.digital_pin2_output.read()), True)

            if self.dig_pin3_prev_status.get() != self.digPinStatus(self.digital_pin3_output.read()):
                self.setDigBitColor(self.dig_pin3, self.dig_pin3_prev_status, self.dig_pin3_radio_status,
                                    self.dig_pin3_radio_off_status, self.digPinStatus(self.digital_pin3_output.read()), True)

            if self.dig_pin4_prev_status.get() != self.digPinStatus(self.digital_pin4_output.read()):
                self.setDigBitColor(self.dig_pin4, self.dig_pin4_prev_status, self.dig_pin4_radio_status,
                                    self.dig_pin4_radio_off_status, self.digPinStatus(self.digital_pin4_output.read()), True)

            if self.dig_pin5_prev_status.get() != self.digPinStatus(self.digital_pin5_output.read()):
                self.setDigBitColor(self.dig_pin5, self.dig_pin5_prev_status, self.dig_pin5_radio_status,
                                    self.dig_pin5_radio_off_status, self.digPinStatus(self.digital_pin5_output.read()), True)

            if self.dig_pin6_prev_status.get() != self.digPinStatus(self.digital_pin6_output.read()):
                self.setDigBitColor(self.dig_pin6, self.dig_pin6_prev_status, self.dig_pin6_radio_status,
                                    self.dig_pin6_radio_off_status, self.digPinStatus(self.digital_pin6_output.read()), True)

            if self.dig_pin7_prev_status.get() != self.digPinStatus(self.digital_pin7_output.read()):
                self.setDigBitColor(self.dig_pin7, self.dig_pin7_prev_status, self.dig_pin7_radio_status,
                                    self.dig_pin7_radio_off_status, self.digPinStatus(self.digital_pin7_output.read()), True)

            if self.dig_pin8_prev_status.get() != self.digPinStatus(self.digital_pin8_output.read()):
                self.setDigBitColor(self.dig_pin8, self.dig_pin8_prev_status, self.dig_pin8_radio_status,
                                    self.dig_pin8_radio_off_status, self.digPinStatus(self.digital_pin8_output.read()), True)

            if self.dig_pin9_prev_status.get() != self.digPinStatus(self.digital_pin9_output.read()):
                self.setDigBitColor(self.dig_pin9, self.dig_pin9_prev_status, self.dig_pin9_radio_status,
                                    self.dig_pin9_radio_off_status, self.digPinStatus(self.digital_pin9_output.read()), True)

            if self.dig_pin10_prev_status.get() != self.digPinStatus(self.digital_pin10_output.read()):
                self.setDigBitColor(self.dig_pin10, self.dig_pin10_prev_status, self.dig_pin10_radio_status,
                                    self.dig_pin10_radio_off_status, self.digPinStatus(self.digital_pin10_output.read()), True)

            if self.dig_pin11_prev_status.get() != self.digPinStatus(self.digital_pin11_output.read()):
                self.setDigBitColor(self.dig_pin11, self.dig_pin11_prev_status, self.dig_pin11_radio_status,
                                    self.dig_pin11_radio_off_status, self.digPinStatus(self.digital_pin11_output.read()), True)

            if self.dig_pin12_prev_status.get() != self.digPinStatus(self.digital_pin12_output.read()):
                self.setDigBitColor(self.dig_pin12, self.dig_pin12_prev_status, self.dig_pin12_radio_status,
                                    self.dig_pin12_radio_off_status, self.digPinStatus(self.digital_pin12_output.read()), True)

            if self.dig_pin13_prev_status.get() != self.digPinStatus(self.digital_pin13_output.read()):
                self.setDigBitColor(self.dig_pin13, self.dig_pin13_prev_status, self.dig_pin13_radio_status,
                                    self.dig_pin13_radio_off_status, self.digPinStatus(self.digital_pin13_output.read()), True)

            #read Analog ports
            time.sleep(2)
            self.readAnalogData(self.analog_pin0_reading, self.analog_pin0_input.read())
            self.readAnalogData(self.analog_pin1_reading, self.analog_pin1_input.read())
            self.readAnalogData(self.analog_pin2_reading, self.analog_pin2_input.read())
            self.readAnalogData(self.analog_pin3_reading, self.analog_pin3_input.read())
            #self.readAnalogData(self.analog_pin4_reading, self.analog_pin4_input.read())
            #self.readAnalogData(self.analog_pin5_reading, self.analog_pin5_input.read())

    def syncWithAurdino(self):

          try:
                if self.syncWithBoardOnce is False:
                    self.syncWithBoardOnce = True
                    self.initBoardPins()

                if self.initSuccess is True:
                    self.keepReadingDigiBitsForEver()
                     #threadObj = threading.Thread(target=self.keepReadingDigiBitsForEver())
                     #threadObj.start()
                     #threadObj.join()

          except Exception as e:
               messagebox.showerror("Error", str(e))
               sys.exit(0)

    def writeToBoard(self):

        try:
            '''if (self.dig_pin0.get() != self.dig_pin0_prev_status.get()):
                self.dig_pin0_prev_status.set(self.dig_pin0.get())
                self.digital_pin0_output.write(int(self.dig_pin0.get()))
                self.setDigBitColor(None, None, self.dig_pin0_radio_status,  self.dig_pin0_radio_off_status, self.dig_pin0.get(), False)

            if (self.dig_pin1.get() != self.dig_pin1_prev_status.get()):
                self.dig_pin1_prev_status.set(self.dig_pin1.get())
                self.digital_pin1_output.write(int(self.dig_pin1.get()))
                self.setDigBitColor(self.dig_pin1_radio_status,  self.dig_pin1_radio_off_status,self.dig_pin1.get())'''

            if (self.dig_pin2.get() != self.dig_pin2_prev_status.get()):
                self.dig_pin2_prev_status.set(self.dig_pin2.get())
                self.digital_pin2_output.write(int(self.dig_pin2.get()))
                self.setDigBitColor(None, None, self.dig_pin2_radio_status,  self.dig_pin2_radio_off_status,self.dig_pin2.get(), False)

            if (self.dig_pin3.get() != self.dig_pin3_prev_status.get()):
                self.dig_pin3_prev_status.set(self.dig_pin3.get())
                self.digital_pin3_output.write(int(self.dig_pin3.get()))
                self.setDigBitColor(None, None, self.dig_pin3_radio_status,  self.dig_pin3_radio_off_status,self.dig_pin3.get(), False)

            if (self.dig_pin4.get() != self.dig_pin4_prev_status.get()):
                self.dig_pin4_prev_status.set(self.dig_pin4.get())
                self.digital_pin4_output.write(int(self.dig_pin4.get()))
                self.setDigBitColor(None, None, self.dig_pin4_radio_status,  self.dig_pin4_radio_off_status,self.dig_pin4.get(), False)

            if (self.dig_pin5.get() != self.dig_pin5_prev_status.get()):
                self.dig_pin5_prev_status.set(self.dig_pin5.get())
                self.digital_pin5_output.write(int(self.dig_pin5.get()))
                self.setDigBitColor(None, None, self.dig_pin5_radio_status,  self.dig_pin5_radio_off_status,self.dig_pin5.get(), False)

            if (self.dig_pin6.get() != self.dig_pin6_prev_status.get()):
                self.dig_pin6_prev_status.set(self.dig_pin6.get())
                self.digital_pin6_output.write(int(self.dig_pin6.get()))
                self.setDigBitColor(None, None, self.dig_pin6_radio_status,  self.dig_pin6_radio_off_status,self.dig_pin6.get(), False)

            if (self.dig_pin7.get() != self.dig_pin7_prev_status.get()):
                self.dig_pin7_prev_status.set(self.dig_pin7.get())
                self.digital_pin7_output.write(int(self.dig_pin7.get()))
                self.setDigBitColor(None, None, self.dig_pin7_radio_status,  self.dig_pin7_radio_off_status,self.dig_pin7.get(), False)

            if (self.dig_pin8.get() != self.dig_pin8_prev_status.get()):
                self.dig_pin8_prev_status.set(self.dig_pin8.get())
                self.digital_pin8_output.write(int(self.dig_pin8.get()))
                self.setDigBitColor(None, None, self.dig_pin8_radio_status,  self.dig_pin8_radio_off_status,self.dig_pin8.get(), False)

            if (self.dig_pin9.get() != self.dig_pin9_prev_status.get()):
                self.dig_pin9_prev_status.set(self.dig_pin9.get())
                self.digital_pin9_output.write(int(self.dig_pin9.get()))
                self.setDigBitColor(None, None, self.dig_pin9_radio_status,  self.dig_pin9_radio_off_status,self.dig_pin9.get(), False)

            if (self.dig_pin10.get() != self.dig_pin10_prev_status.get()):
                self.dig_pin10_prev_status.set(self.dig_pin10.get())
                self.digital_pin10_output.write(int(self.dig_pin10.get()))
                self.setDigBitColor(None, None, self.dig_pin10_radio_status,  self.dig_pin10_radio_off_status,self.dig_pin10.get(), False)

            if (self.dig_pin11.get() != self.dig_pin11_prev_status.get()):
                self.dig_pin11_prev_status.set(self.dig_pin11.get())
                self.digital_pin11_output.write(int(self.dig_pin11.get()))
                self.setDigBitColor(None, None, self.dig_pin11_radio_status,  self.dig_pin11_radio_off_status,self.dig_pin11.get(), False)

            if (self.dig_pin12.get() != self.dig_pin12_prev_status.get()):
                self.dig_pin12_prev_status.set(self.dig_pin12.get())
                self.digital_pin12_output.write(int(self.dig_pin12.get()))
                self.setDigBitColor(None, None, self.dig_pin12_radio_status,  self.dig_pin12_radio_off_status,self.dig_pin12.get(), False)

            if (self.dig_pin13.get() != self.dig_pin13_prev_status.get()):
                self.dig_pin13_prev_status.set(self.dig_pin13.get())
                self.digital_pin13_output.write(int(self.dig_pin13.get()))
                self.setDigBitColor(None, None, self.dig_pin13_radio_status,  self.dig_pin13_radio_off_status,self.dig_pin13.get(), False)

        except Exception as e:
            messagebox.showerror("Error", "Please press \"Sync with Arduino\" button first if you have missed.")

if __name__ == '__main__':


    # Removes the maximizing option
    #root.resizable(0, 0)

    root = tk.Tk()
    # Change the background window color
    root.configure(background='#b7bbc7')
    root.state('zoomed')

    # Set window parameters
    root.geometry('850x620')
    root.title('Arduino Board Control Operations')
    ObjController = GUI_COntroller(root)

    # keep the main window is running
    root.mainloop()



