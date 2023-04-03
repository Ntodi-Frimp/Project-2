import PySimpleGUI as psg
import pyttsx3

psg.theme('Dark blue 3')
layout = [
    [psg.Input(key='char'), psg.Button('speak',key= 'start_button')],
    [psg.Text('select voice type', background_color= '#000000'), psg.Radio('Male','Gender',key='Male_voice', default=True,background_color= '#000000'), psg.Radio('Female','Gender',key ='Female_voice',background_color= '#000000')],
    [psg.Text('speed ', background_color='#000000'), psg.Input(key='speed_rate',size=4, default_text='100')],
    [psg.Text('Volume'), psg.Slider(key='volume', range=(0,10), orientation='hor',size=(10,10), default_value= 0)]
]





class Speech_conv:
    def Voice_type(input_type, voice_type, speed_rate, volume):
            speech= pyttsx3.init()
            voices= speech.getProperty('voices')
            speech.setProperty('voice',voices[voice_type].id)
            speech.setProperty('rate',speed_rate)
            speech.setProperty('volume',volume)
            speech.say(input_type)
            speech.runAndWait()


window=psg.Window('Text to speech App', layout)



while True:
    event,values = window.read()
    if event== psg.WIN_CLOSED:
        break

    input= values['char']
    speed_r= int(values['speed_rate'])
    speech_vol= int(values['volume'] )


    if event=='start_button':
         if values['Male_voice'] ==True:
              Speech_conv.Voice_type(input_type=input,voice_type=0,speed_rate=speed_r,volume=speech_vol)

         if values['Female_voice'] == True:
              Speech_conv.Voice_type(input_type=input,voice_type=1,speed_rate=speed_r,volume=speech_vol)






    input = values['char']
    Speed_r= int(values['speed_rate'])
    Speech_vol= int(values['volume']) * 0.1
      

    if event== 'start_button':
        if values['Male_voice']==True:
            input= values['char']