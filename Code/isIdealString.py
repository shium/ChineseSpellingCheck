stop_symbols = [".", ",","。","#", "\n", "(", "、", "`", "，", \
"##","$","###","####", "-", "+","|","/", ":", "：","*","?","!","@", \
"#"," ","\'","\"","\\",";","%",")","(","<",">","？","！","；","「","」","（","）" \
"[","]","{","}","“","”","）","《","》","=","\t","】","__"]

def isIdealString(word, PreviousWord):
    if PreviousWord not in stop_symbols \
    and word not in stop_symbols \
    and not word[0].encode('utf8').isalpha() \
    and not PreviousWord[0].encode('utf8').isalpha() \
    and not word[0].isdigit() \
    and not PreviousWord[0].isdigit():
        return True
    else:
        return False