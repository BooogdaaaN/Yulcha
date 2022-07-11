import lyricsgenius
from operator import itemgetter
from collections import Counter
genius = lyricsgenius.Genius("ZhHEMz4EEjfKhF_e7cVXVaxJHqvULU8_a-0bKCZSCmhWMVs0ymsujj6PtcW10TCJ")
artist = genius.search_artist("dead blonde",max_songs=50,sort="popularity")

unredacted1=''
for song in artist.songs:
    unredacted1+=song.lyrics
    unredacted1 +="["

# remove []
redactedLyrics = ''
for i in range(0,len(unredacted1)):
    if unredacted1[i] == "]":
        for j in range(i,len(unredacted1)):
            if unredacted1[j] =="[":
                redactedLyrics += unredacted1[i+1:j]
                break

# remove ()
unredacted2 = ")" + redactedLyrics + "("
redactedLyrics = ''
for i in range(0,len(unredacted2)):
    if unredacted2[i] == ")":
        for j in range(i,len(unredacted2)):
            if unredacted2[j] =="(":
                redactedLyrics += unredacted2[i+1:j]
                break

redactedLyrics = redactedLyrics.replace('\n'," ")
redactedLyrics = redactedLyrics.lower()
redactedLyrics = redactedLyrics.replace("Embed", '  ')
redactedLyrics = redactedLyrics.replace("embed", '  ')
redactedLyrics = redactedLyrics.replace("—", ' ')
redactedLyrics = redactedLyrics.replace(" на ", ' ')
redactedLyrics = redactedLyrics.replace(" не ", ' ')
redactedLyrics = redactedLyrics.replace(" в ", ' ')
redactedLyrics = redactedLyrics.replace(" и ", ' ')
redactedLyrics = redactedLyrics.replace(" под ", ' ')
redactedLyrics = redactedLyrics.replace(" над ", ' ')
redactedLyrics = redactedLyrics.replace(" что ", ' ')
redactedLyrics = redactedLyrics.replace(" это ", ' ')
redactedLyrics = redactedLyrics.replace(" как ", ' ')
redactedLyrics = redactedLyrics.replace(" да ", ' ')
redactedLyrics = redactedLyrics.replace(" я ", '')
redactedLyrics = redactedLyrics.replace(" м ", ' ')
redactedLyrics = redactedLyrics.replace(" е ", ' ')
redactedLyrics = redactedLyrics.replace(" с ", ' ')
redactedLyrics = redactedLyrics.replace(" у ", ' ')
redactedLyrics = redactedLyrics.replace(" но ", ' ')
redactedLyrics = redactedLyrics.replace(" от ", ' ')
redactedLyrics = redactedLyrics.replace(" , ", ' ')
redactedLyrics = redactedLyrics.replace(" а ", ' ')
redactedLyrics = redactedLyrics.replace(" то ", ' ')
redactedLyrics = redactedLyrics.replace(" как ", ' ')
redactedLyrics = redactedLyrics.replace(",", '')
redactedLyrics = redactedLyrics.replace("?", '')
redactedLyrics = redactedLyrics.replace(" меня ", ' ')
redactedLyrics = redactedLyrics.replace(" я ", ' ')
redactedLyrics = redactedLyrics.replace(" мне ", ' ')
redactedLyrics = redactedLyrics.replace(" так ", ' ')
redactedLyrics = redactedLyrics.replace(" ты ", ' ')
redactedLyrics = redactedLyrics.replace(" мы ", ' ')
redactedLyrics = redactedLyrics.replace(" то ", ' ')
redactedLyrics = redactedLyrics.replace(" эти ", ' ')
redactedLyrics = redactedLyrics.replace(" это ", ' ')
redactedLyrics = redactedLyrics.replace(" вот ", ' ')
redactedLyrics = redactedLyrics.replace(" со ", ' ')
redactedLyrics = redactedLyrics.replace(" ли ", ' ')
redactedLyrics = redactedLyrics.replace(" из ", ' ')
redactedLyrics = redactedLyrics.replace(" все ", ' ')
redactedLyrics = redactedLyrics.replace(" без ", ' ')
redactedLyrics = redactedLyrics.replace(" мой ", ' ')
redactedLyrics = redactedLyrics.replace(" моё ", ' ')
redactedLyrics = redactedLyrics.replace(" моей ", ' ')
redactedLyrics = redactedLyrics.replace(" моём ", ' ')
redactedLyrics = redactedLyrics.replace(" мои ", ' ')
redactedLyrics = redactedLyrics.replace(" ну ", ' ')
redactedLyrics = redactedLyrics.replace(" бы ", ' ')
redactedLyrics = redactedLyrics.replace(" моя ", ' ')
redactedLyrics = redactedLyrics.replace(" всё ", ' ')
redactedLyrics = redactedLyrics.replace(" он ", ' ')
redactedLyrics = redactedLyrics.replace(" за ", ' ')
redactedLyrics = redactedLyrics.replace(" если ", ' ')
redactedLyrics = redactedLyrics.replace(" по ", ' ')
redactedLyrics = redactedLyrics.replace(" же ", ' ')
redactedLyrics = redactedLyrics.replace(" кто ", ' ')
redactedLyrics = redactedLyrics.replace(" для ", ' ')
redactedLyrics = redactedLyrics.replace(" уже ", ' ')
redactedLyrics = redactedLyrics.replace(" нам ", ' ')
redactedLyrics = redactedLyrics.replace(" до ", ' ')
redactedLyrics = redactedLyrics.replace(" твоя ", ' ')
redactedLyrics = redactedLyrics.replace(" твой ", ' ')
redactedLyrics = redactedLyrics.replace(" твои ", ' ')
redactedLyrics = redactedLyrics.replace(" твоей ", ' ')
redactedLyrics = redactedLyrics.replace(" нас ", ' ')
redactedLyrics = redactedLyrics.replace(" твоё ", ' ')
redactedLyrics = redactedLyrics.replace(" тебя ", ' ')
redactedLyrics = redactedLyrics.replace(" про ", ' ')
redactedLyrics = redactedLyrics.replace(" ни ", ' ')
redactedLyrics = redactedLyrics.replace(" нет ", ' ')
redactedLyrics = redactedLyrics.replace(" i ", ' ')
redactedLyrics = redactedLyrics.replace(" me ", ' ')
redactedLyrics = redactedLyrics.replace(" mine ", ' ')
redactedLyrics = redactedLyrics.replace(" my ", ' ')
redactedLyrics = redactedLyrics.replace(" you ", ' ')
redactedLyrics = redactedLyrics.replace(" your ", ' ')
redactedLyrics = redactedLyrics.replace(" yours ", ' ')
redactedLyrics = redactedLyrics.replace(" he ", ' ')
redactedLyrics = redactedLyrics.replace(" him ", ' ')
redactedLyrics = redactedLyrics.replace(" his ", ' ')
redactedLyrics = redactedLyrics.replace(" she ", ' ')
redactedLyrics = redactedLyrics.replace(" her ", ' ')
redactedLyrics = redactedLyrics.replace(" it ", ' ')
redactedLyrics = redactedLyrics.replace(" its ", ' ')
redactedLyrics = redactedLyrics.replace(" it's ", ' ')
redactedLyrics = redactedLyrics.replace(" i'm ", ' ')
redactedLyrics = redactedLyrics.replace(" you're ", ' ')
redactedLyrics = redactedLyrics.replace(" u ", ' ')
redactedLyrics = redactedLyrics.replace(" a ", ' ')
redactedLyrics = redactedLyrics.replace(" the ", ' ')
redactedLyrics = redactedLyrics.replace(" an ", ' ')
redactedLyrics = redactedLyrics.replace(" do ", ' ')
redactedLyrics = redactedLyrics.replace(" does ", ' ')
redactedLyrics = redactedLyrics.replace(" and ", ' ')
redactedLyrics = redactedLyrics.replace(" or ", ' ')
redactedLyrics = redactedLyrics.replace(" my ", ' ')
redactedLyrics = redactedLyrics.replace("!", ' ')
redactedLyrics = redactedLyrics.replace(" 2] ", ' ')
redactedLyrics = redactedLyrics.replace("  ", " ")
redactedLyrics = redactedLyrics.replace("   ", " ")
redactedLyrics = redactedLyrics.replace("    ", " ")

# Functions

def count_words(s, n):
    words = s.split(" ");
    words = Counter(words)
    top_n = words.most_common(n)
    return top_n

words = count_words(redactedLyrics, 100)












# with open('allLyrics.txt', 'w',encoding="utf-8") as outfile:
# outfile.write(s)