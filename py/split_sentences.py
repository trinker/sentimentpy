# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:07:23 2018

@author: trinker
"""

import re
import numpy as np


abbr_rep_1_json = {
    "Titles": [
        "[mM]r",
        "[mM]rs",
        "[mM]s",
        "[dD]r",
        "[pP]rof",
        "[sS]en",
        "[rR]ep",
        "[rR]ev",
        "[gG]ov",
        "[aA]tty",
        "[sS]upt",
        "[dD]et",
        "[rR]ev",
        "[cC]ol",
        "[gG]en",
        "[lL]t",
        "[cC]mdr",
        "[aA]dm",
        "[cC]apt",
        "[sS]gt",
        "[cC]pl",
        "[mM]aj"
    ],
    "Entities": [
        "[dD]ept",
        "[uU]niv",
        "[uU]ni",
        "[aA]ssn"
    ],
    "Misc": [
        "[vV]s",
        "[mM]t"
    ],
    "Streets": [
        "[sS]t"
    ]
}


abbr_rep_2_json = {
    "Titles": [
        "[jJ]r",
        "[sS]r"
    ],
    "Entities": [
        "[bB]ros",
        "[iI]nc",
        "[lL]td",
        "[cC]o",
        "[cC]orp",
        "[pP]lc"
    ],
    "Months": [
        "[jJ]an",
        "[fF]eb",
        "[mM]ar",
        "[aA]pr",
        "[mM]ay",
        "[jJ]un",
        "[jJ]ul",
        "[aA]ug",
        "[sS]ep",
        "[oO]ct",
        "[nN]ov",
        "[dD]ec",
        "[sS]ept"
    ],
    "Days": [
        "[mM]on",
        "[tT]ue",
        "[wW]ed",
        "[tT]hu",
        "[fF]ri",
        "[sS]at",
        "[sS]un"
    ],
    "Misc": [
        "[eE]tc",
        "[eE]sp",
        "[cC]f",
        "[aA]l"
    ],
    "Streets": [
        "[aA]ve",
        "[bB]ld",
        "[bB]lvd",
        "[cC]l",
        "[cC]t",
        "[cC]res",
        "[rR]d"
    ],
    "Measurement": [
        "[fF]t",
        "[gG]al",
        "[mM]i",
        "[tT]bsp",
        "[tT]sp",
        "[yY]d",
        "[qQ]t",
        "[sS]q",
        "[pP]t",
        "[lL]b",
        "[lL]bs"
    ]
}


  
period_reg = '{}|{}|{}|{}'.format(
    r"(?:(?<=[a-z])\.\s(?=[a-z]\.))",
    r"(?:(?<=([ .][a-z]))\.)(?!(?:\s[A-Z]|$)|(?:\s\s))",
    r"(?:(?<=[A-Z])\.(?=\s??[A-Z]\.))",
    r"(?:(?<=[A-Z])\.(?!\s+[A-Z][A-Za-z]))"
)



abbr_rep_1 = [item for sublist in list(abbr_rep_1_json.values()) for item in sublist]
abbr_rep_1_results = []

for i in range(len(abbr_rep_1)):
    abbr_rep_1_results.append(r"((?<=\b({}))\.)".format(abbr_rep_1[i]))
    


abbr_rep_2 = [item for sublist in list(abbr_rep_2_json.values()) for item in sublist]        
abbr_rep_2_results = []

for i in range(len(abbr_rep_2)):
    abbr_rep_2_results.append(r"((?<=\b({}))\.(?!\s+[A-Z]))".format(abbr_rep_2[i]))
    

sent_regex = "{}|{}|{}|({})".format(
    "|".join(abbr_rep_1_results),
    "|".join(abbr_rep_2_results),
    period_reg,
    r'\.(?=\d+)'
)




## This works on a single string.  Need to loop through and apply.
def break_sentence(x):

    y = re.sub(
        pattern = r'([Pp])(\.)(\s*[Ss])(\.)', 
        repl = r'\1<<<TEMP>>>\3<<<TEMP>>>',
        string = x.strip()
    )
    
    y = re.sub(
        pattern = sent_regex, 
        repl = "<<<TEMP>>>",
        string = y
    )
    
    y = re.sub(
        pattern = r'(\b[Nn]o)(\\.)(\s+\d)', 
        repl = r'\1<<<TEMP>>>\3',
        string = y
    )
    
    y = re.sub(
        pattern = r'(\b\d+\s+in)(\.)(\s[a-z])', 
        repl = r'\1<<<TEMP>>>\3',
        string = y
    )
    
    y = re.sub( 
        pattern = r'([?.!]+)([\'])([^,])', 
        repl = r'<<<SQUOTE>>>\1  \3',
        string = y
    )
    
    y = re.sub(  
        pattern = r'([?.!]+)(["])([^,])', 
        repl = r'<<<DQUOTE>>>\1  \3',
        string = y
    )
    
    ## midde name handling
    y = re.sub( 
        pattern = r'(\b[A-Z][a-z]+\s[A-Z])(\.)(\s[A-Z][a-z]+\b)',
        repl = r'\1<<<TEMP>>>\3',
        string = y
    )

    #2 middle names
    y = re.sub( 
        pattern = r'(\b[A-Z][a-z]+\s[A-Z])(\.)(\s[A-Z])(\.)(\s[A-Z][a-z]+\b)',
        repl = r'\1<<<TEMP>>>\3<<<TEMP>>>\5',
        string = y
    )
    
    y = re.split( 
        pattern = r"{}{}".format(
            r"(?:(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?!])(?:\s|",  
            r"(?=[a-zA-Z][a-zA-Z]*\s)))|(?:(?<=[A-Z][a-z][.?!])\s+)"
        ),
        string = y
    )
            
    return y


## break a single string into sentences
## TO DO: handling missing????
def break_sentences(x):
    
    broken_results = []

    for i in range(len(x)):
        broken_results.append(break_sentence(x[i]))
        
    return broken_results



def restore_sentence(x):

    ## pdb.set_trace()
    y = re.sub( 
        pattern = r'<<<TEMP>>>',
        repl = r'.',
        string = x.strip()
    )
    
    y = re.sub( 
        pattern = r'(<<<DQUOTE>>>)([?.!]+)',
        repl = r'\2"',
        string = y
    )

    y = re.sub( 
        pattern = r'(<<<SQUOTE>>>)([?.!]+)',
        repl = r'\2\"',
        string = y
    )
    
    return y
    



def split_sentences(x):
    
    y = break_sentences(x)    
       
    element_id = np.repeat(range(len(y)), [len(i) for i in y])
    sentence_id = [range(len(i)) for i in y]
    sentence_id = [item for sublist in sentence_id for item in sublist]
     
#    locs = (np.cumsum([len(x) for x in y]) + 1)[:-1]
## TO DO: this should returna pandas object with an element_id, sentence_id, and the text

    sents = [restore_sentence(sentence).strip() for element in y for sentence in element]
    return sents

## Identical to ^^^
# =============================================================================
# list_of_words = []
# for element in y:
#     for sentence in element:
#        list_of_words.append(restore_sentence(sentence))
# 
# list_of_words
# =============================================================================


if __name__ == '__main__':
    # --- examples -------
    s = [
        ' I like you.  P.S. I like carrots too mrs. dunbar. Well let\'s go to 100th st. around the corner.   ', 
        'Hello Dr. Livingstone.  How are you?', 
        'This is sill an incomplete thou.'
        
    ]

    split_sentences(s)








