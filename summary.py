#Steps for Text Summarization

#Text Cleaning
#Sentence Tokenization
#Word  Tokenization
#World Frequency Table
#Sentence Score Calculation
#Picking Up Sentences


from mimetypes import init


class TEXTE:

    def __init__(self,text):
        self.text=text

    def summary(self): 
             #Imnporting Neccesary Modules
             import spacy 
             from spacy.lang.en.stop_words import STOP_WORDS
             from string import punctuation
             from heapq import nlargest

             stopwords=list(STOP_WORDS)

             #CREATING NLP MODEL

             nlp=spacy.load('en_core_web_sm')

             #MAKING A  DUMMY TEXT



            #WORD TOKENIZATION
             doc=nlp(self.text)

             tokens=[token.text for token in doc ]

             punctuation+="\n"

             #creating a word frequency dictionary
             word_frequency={}

             for word in doc:
                if word.text.lower() not in stopwords:
                    if word.text.lower() not in punctuation:
                        if word.text.lower not in word_frequency.keys():
                            word_frequency[word.text]=1
                        else:
                            word_frequency[word.text]+=1

            #frequency normalization
             max_frequency=max(word_frequency.values())

             for word in word_frequency.keys():
                  word_frequency[word]=word_frequency[word]/max_frequency

            #sentence tokenization
             sentence_tokens=[sent for sent in doc.sents]


            #computing senetence score 

             sentence_score={}
             for sent in sentence_tokens:
                for word in sent:
                   if word.text.lower() in word_frequency.keys():
                      if sent not in sentence_score.keys():
                        sentence_score[sent]=word_frequency[word.text.lower()]
                      else:
                        sentence_score[sent]+=word_frequency[word.text.lower()]

            #picking up sentences
                select_length=int(len(sentence_score)*0.3)

 
              #Making the summary

             summary=nlargest(select_length,sentence_score,key=sentence_score.get)


             final_summary=[word.text for word in summary]

             summary=" ".join(final_summary)

            

             
            
             
             return summary
            

if __name__=="__main__":
    pass
else:
    pass