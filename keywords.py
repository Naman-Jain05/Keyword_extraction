#importing the required modules
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


#fetching transcript online with the help of youtube id
from youtube_transcript_api import YouTubeTranscriptApi 
transcript_data = YouTubeTranscriptApi.get_transcript("gBd-ct58DCI") #transcript of given youtube video given in exercise problem 
print(transcript_data)

#extracting text from the transcript file parsing the json file to string
n=len(transcript_data)
text=""
for i in range(n):
  text += (transcript_data[i].get('text'))
print(text)  

#another method of getting the text from the youtube video
f=open('trans.txt')#by default  mode is read
data=f.read()
print(data)

#summarising the text by 0.5 ratio
print(summarize(text, ratio=0.5))

#summarising and splitting into list
print(summarize(text, split=True, ratio=0.5))

#printing top 50 keywords
ans=keywords(text, words=50)
print(ans)

#displaying the keywords in a new text file
fl=open("uncreated.txt","w")
fl.write(ans)
fl.close()
f.close()

#summarising keywords
from gtts import gTTS
text_to_say ="key-words"+"are"+ ans
language = "en"
gtts_object = gTTS(text = text_to_say,  lang = language,slow = False)
gtts_object.save("/content/gtts.wav")
from IPython.display import Audio
Audio("/content/gtts.wav")