'''
##############################
#Todo:
#Check valid APCO-25 vocoder in case invalid bitrate
#Assign usual bitrate for P25: 9600 bps
##############################

#imports
import wave
import pyaudio

#Constants
APCO_25_BITRATE = 9600 #bps

#decoder
def Apco25ToP25Decoder(wav_file):
	#open wav file
	audio = wave.open(wav_file, 'rb')
	#create a pyaudio instance
	p = pyaudio.PyAudio()
	#load the APCO-25 bitrate
	rate = audio.getframerate()
	#if it's not set to the APCO-25 bitrate, assign the rate to the typical P25 bitrate (9600 bps)
	if rate != APCO_25_BITRATE:
		rate = APCO_25_BITRATE
	#open audio stream with PyAudio
	stream = p.open(format=p.get_format_from_width(audio.getsampwidth()),
					channels=audio.getnchannels(),
					rate=rate,
					output=True)
	#read data and write it to the pyaudio output stream
	data = audio.readframes(1024)
	while data:
		stream.write(data)
		data = audio.readframes(1024)
	#stop the audio stream
	stream.stop_stream()
	stream.close()
	#close pyaudio
	p.terminate()