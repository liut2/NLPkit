import re
# stemmer.py
# written by Sherry Gu and Tao Liu
# This function takes as input a string, and returns the stemmed version of that string.
def stem(user_input):
    step1_result = step1(user_input)
    step2_result = step2(step1_result)
    step3_result = step3(step2_result)
    step4_result = step4(step3_result)
    step5_result = step5(step4_result)
    print(step5_result)
#this function implements the algorithm in step1 and return the result   
def step1(word):
    #step1a
    if re.search("sses$", word):
        word = re.sub("sses$", "ss", word)
    elif re.search("ies$", word):
        word = re.sub("ies$", "i", word)
    elif re.search("ss$", word):
        word = re.sub("ss$", "ss", word)
    elif re.search("s$", word):
        word = re.sub("s$", "", word)
    #step1b
    ifHasFollowing = False
    if re.search("eed$", word):
        temp = re.sub("eed$", "", word)
        if countMeasure(temp) > 0:
            word = re.sub("eed$", "ee", word)
    elif re.search("ed$", word):
        temp = re.sub("ed$", "", word)
        if re.search("[aeiou]|[^aeiou]y", temp):
            word = re.sub("ed$", "", word)
            ifHasFollowing = True
    elif re.search("ing$", word):
        temp = re.sub("ing$", "", word)
        if re.search("[aeiou]|[^aeiou]y", temp):
            word = re.sub("ing$", "", word)
            ifHasFollowing = True

    #following check
    if ifHasFollowing == True:
        if re.search("at$", word):
            word = re.sub("at$", "ate", word)
        elif re.search("bl$", word):
            word = re.sub("bl$", "ble", word)
        elif re.search("iz$", word):
            word = re.sub("iz$", "ize", word)
        elif re.search("[^aeiou]{2}$", word) and re.search("[^lsz]$", word):
            word = re.sub("[^aeiou]$", "", word)
        elif countMeasure(word) == 1 and ifEndWithCVC(word):
        	word += "e"
    #step1c
    if re.search("y$", word):
        temp = re.sub("y$", "", word)
        if re.search("[aeiou]|[^aeiou]y", temp):
            word = re.sub("y$", "i", word)
            
    return word
# this function checks whether a word satisfy *o*, which is "end with cvc, but the 
# second c is not w,x or y"      
def ifEndWithCVC(word):
	VCPattern = ""
	for i in range(0, len(word)):
		if re.match("[^aeiou]", word[i]):
			if (i != 0) and re.match("[^aeiou]y", word[i-1]+word[i]):
				VCPattern += "V"
			else:
				VCPattern += "C"
		else:
			VCPattern += "V"

	if re.search("CVC$", VCPattern) and re.search("[^wxy]$",word ):
		return True
	return False
# this function calculates the measure of the stem and return the count
def countMeasure(word):
    VCPattern = ""
    for i in range(0, len(word)):
        if re.match("[^aeiou]", word[i]):
            if (i != 0) and re.match("[^aeiou]y", word[i-1]+word[i]):
                VCPattern += "V"
            else:
                VCPattern += "C"
        else:
            VCPattern += "V"

    count = len(re.findall(r"V+C+", VCPattern))
    return count
# this function implements algorithm in step2          
def step2(step1_result):
    if re.search(r"ational$",step1_result):
        m = countMeasure(re.sub(r"ational$","",step1_result))
        if m > 0:
            return re.sub(r"ational$","ate",step1_result)

    elif re.search(r"tional$",step1_result):
        m = countMeasure(re.sub(r"tional$","",step1_result))
        if m > 0:
            return re.sub(r"tional$","tion",step1_result)

    elif re.search(r"enci$",step1_result):
        m = countMeasure(re.sub(r"enci$","",step1_result))
        if m > 0:
            return re.sub(r"enci$","ence",step1_result)
        
    elif re.search(r"anci$",step1_result):
        m = countMeasure(re.sub(r"anci$","",step1_result))
        if m > 0:
            return re.sub(r"anci$","ance",step1_result)

    elif re.search(r"izer$",step1_result):
        m = countMeasure(re.sub(r"izer$","",step1_result))
        if m > 0:
            return re.sub(r"izer$","ize",step1_result)

    elif re.search(r"abli$",step1_result):
        m = countMeasure(re.sub(r"abli$","",step1_result))
        if m > 0:
            return re.sub(r"abli$","able",step1_result)

    elif re.search(r"alli$",step1_result):
        m = countMeasure(re.sub(r"alli$","",step1_result))
        if m > 0:
            return re.sub(r"alli$","al",step1_result)


    elif re.search(r"entli$",step1_result):
        m = countMeasure(re.sub(r"entlil$","",step1_result))
        if m > 0:
            return re.sub(r"entli$","ent",step1_result)


    elif re.search(r"eli$",step1_result):
        m = countMeasure(re.sub(r"eli$","",step1_result))
        if m > 0:
            return re.sub(r"eli$","e",step1_result)

    elif re.search(r"ousli$",step1_result):
        m = countMeasure(re.sub(r"ousli$","",step1_result))
        if m > 0:
            return re.sub(r"ousli$","ous",step1_result)

    elif re.search(r"ization$",step1_result):
        m = countMeasure(re.sub(r"ization$","",step1_result))
        if m > 0:
            return re.sub(r"ization$","ize",step1_result)

    elif re.search(r"ation$",step1_result):
        m = countMeasure(re.sub(r"ation$","",step1_result))
        if m > 0:
            return re.sub(r"ation$","ate",step1_result)

    elif re.search(r"ator$",step1_result):
        m = countMeasure(re.sub(r"ator$","",step1_result))
        if m > 0:
            return re.sub(r"ator$","ate",step1_result)

    elif re.search(r"alism$",step1_result):
        m = countMeasure(re.sub(r"alism$","",step1_result))
        if m > 0:
            return re.sub(r"alism$","al",step1_result)

    elif re.search(r"iveness$",step1_result):
        m = countMeasure(re.sub(r"iveness$","",step1_result))
        if m > 0:
            return re.sub(r"iveness$","ive",step1_result)

    elif re.search(r"fulness$",step1_result):
        m = countMeasure(re.sub(r"fulness$","",step1_result))
        if m > 0:
            return re.sub(r"fulness$","ful",step1_result)

    elif re.search(r"ousness$",step1_result):
        m = countMeasure(re.sub(r"ousness$","",step1_result))
        if m > 0:
            return re.sub(r"ousness$","ous",step1_result)

    elif re.search(r"aliti$",step1_result):
        m = countMeasure(re.sub(r"aliti$","",step1_result))
        if m > 0:
            return re.sub(r"aliti$","al",step1_result)

    elif re.search(r"iviti$",step1_result):
        m = countMeasure(re.sub(r"iviti$","",step1_result))
        if m > 0:
            return re.sub(r"iviti$","ive",step1_result)

    elif re.search(r"biliti$",step1_result):
        m = countMeasure(re.sub(r"biliti$","",step1_result))
        if m > 0:
            return re.sub(r"biliti$","ble",step1_result)
    return step1_result
# this function implements algorithm in step3
def step3(step2_result):
    if re.search(r"icate$",step2_result):
        m = countMeasure(re.sub(r"icate$","",step2_result))
        if m > 0:
            return re.sub(r"icate$","ic",step2_result)

    if re.search(r"ative$",step2_result):
        m = countMeasure(re.sub(r"ative$","",step2_result))
        if m > 0:
            return re.sub(r"ative$","",step2_result)

    if re.search(r"alize$",step2_result):
        m = countMeasure(re.sub(r"alize$","",step2_result))
        if m > 0:
            return re.sub(r"alize$","al",step2_result)

    if re.search(r"iciti$",step2_result):
        m = countMeasure(re.sub(r"iciti$","",step2_result))
        if m > 0:
            return re.sub(r"iciti$","ic",step2_result)

    if re.search(r"ful$",step2_result):
        m = countMeasure(re.sub(r"ful$","",step2_result))
        if m > 0:
            return re.sub(r"ful$","",step2_result)

    if re.search(r"ness$",step2_result):
        m = countMeasure(re.sub(r"ness$","",step2_result))
        if m > 0:
            return re.sub(r"ness$","",step2_result)

    return step2_result
# this function  implements algorithm in step4
def step4(word):
	if re.search("al$", word):
		temp = re.sub("al$", "", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ance$", word):
		temp = re.sub("ance$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ence$", word):
		temp = re.sub("ence$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("er$", word):
		temp = re.sub("er$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ic$", word):
		temp = re.sub("ic$", "",word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("able$", word):
		temp = re.sub("able$", "",word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ible$", word):
		temp = re.sub("ible$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ant$", word):
		temp = re.sub("ant$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ement$", word):
		temp = re.sub("ement$", "",word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ment$", word):
		temp = re.sub("ment$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ent$", word):
		temp = re.sub("ent$", "",word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ion$", word):
		temp = re.sub("ion$", "",word)
		if countMeasure(temp) > 1 and re.search("[st]$", temp):
			word = temp
	elif re.search("ou$", word):
		temp = re.sub("ou$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ism$", word):
		temp = re.sub("ism$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ate$", word):
		temp = re.sub("ate$", "",word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("iti$", word):
		temp = re.sub("iti$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ous$", word):
		temp = re.sub("ous$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ive$", word):
		temp = re.sub("ive$","", word)
		if countMeasure(temp) > 1:
			word = temp
	elif re.search("ize$", word):
		temp = re.sub("ize$", "",word)
		if countMeasure(temp) > 1:
			word = temp

	return word
# this funciton implements algorithm in step5
def step5(word):
	#step5a
	if re.search("e$", word):
		temp = re.sub("e$", "", word)
		if countMeasure(temp) > 1:
			word = temp
		elif (countMeasure(temp) == 1) and (not ifEndWithCVC(temp)):
			word = temp
	#step5b
	if countMeasure(word) > 1 and re.search("[^aeiou]{2}$", word) and re.search("l$", word):
		word = re.sub("[^aeiou]{2}$", "l", word)
	return word

def main():
	user_input = input('Tell me the word to get stem from.\n').lower()
	stem(user_input)
    
if __name__ == '__main__':
    main()



    
