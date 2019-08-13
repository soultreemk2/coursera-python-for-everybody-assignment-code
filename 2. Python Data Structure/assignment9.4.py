# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
 
for line in handle:
    line.rstrip()
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue #From이 들어간 문장 중 From:는 제외
    words = line.split()
    #if len(words) == 2: continue
    #From:으로 시작하는 라인은 len(words)이 2이기 때문에 9번줄 대신 len(words) == 2 를 제외시켜도 된다
    counts[words[1]] = counts.get(words[1], 0) + 1 #From 다음 단어가 이메일이기 때문에 words[1]
 
maxkey = None
maxvalue = None
for key, value in counts.items():
    if maxkey is None or maxvalue < value: #maxkey가 None인 경우를 제외하지 않으면 maxvalue<value 계산도 불가
        maxkey = key
        maxvalue = value
print(maxkey, maxvalue)


