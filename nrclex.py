from nrclex import NRCLex

text = "I am very happy and excited"

emotion = NRCLex(text)

print(emotion.raw_emotion_scores)