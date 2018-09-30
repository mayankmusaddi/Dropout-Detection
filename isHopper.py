import dateutil.parser as dp
import docx

fname = input()
fname = "../datasets/Hackathon Datasets/ResumeDataset/"+fname+".docx"

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

text = getText(fname)
lines = text.split('\n')
caption = "PROFILE"

exp = []
isHopper = 0
for line in lines:
	words = line.split()
	if len(words) < 4 and len(words) > 0:
		caption = line
	
	if "education" not in caption.lower():
		if "-" in line or "–" in line or "to" in line:
			if "-" in line:
				l = line.split("-")
			if "–" in line:
				l = line.split("–")
			if "to" in line:
				l = line.split("to")
			try:
				date1 = dp.parse(l[0],fuzzy=True)
				date2 = dp.parse(l[1],fuzzy=True)
				# print(date1.year,date1.month,"<-->",date2.year,date2.month)
				diff = (int(date2.year) - int(date1.year))*12 + (int(date2.month)-int(date1.month))
				if diff > 0 :
					exp.append(diff)
					# print(diff)
			except:pass
		else:
			try:
				date = dp.parse(line,fuzzy=True)
				# print(date.year,date.month)
			except:pass

# In an ideal world, you should try to stay at each job for a minimum of two years, according to Amanda Augustine, career advice expert for TopResume.
badexp = [x for x in exp if x < 24]

if len(exp) is 0:
	isHopper = -1 # Unable to Detect
else:
	if len(exp) > 1 and max(exp) < 24 :
		isHopper = 3 # Is a serial job hopper
	if len(exp) > 4 and len(badexp) > 2:
		isHopper = 2 # Has high tendency for hopping
	if len(exp) <= 1 and max(exp) < 24:
		isHopper = 1 # Can be a hopper

print("Job Hopping Tendency (JHT): ",isHopper)