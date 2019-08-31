data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))

wc = {}
for d in data:
	words = d.strip().split()
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請輸入欲查詢的字： ')
	if word == 'q':
		break
	if word in wc:
		print(word, '總共出現', wc[word], '次')
	else:
		print('查無此字！')
print('感謝您的使用')