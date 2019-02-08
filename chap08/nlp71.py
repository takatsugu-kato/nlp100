def isStopWord(word):
    return word.lower() in stop_words

stop_words = "a,did,in,only,then,where,\
all,do,into,onto,there,whether,\
almost,does,is,or,therefore,which,\
also,either,it,our,these,while,\
although,for,its,ours,they,who,\
an,from,just,s,this,whose,\
and,had,ll,shall,those,why,\
any,has,me,she,though,will,\
are,have,might,should,through,with,\
as,having,Mr,since,thus,would,\
at,he,Mrs,so,to,yet,\
be,her,Ms,some,too,you,\
because,here,my,still,until,your,\
been,hers,no,such,ve,yours,\
both,him,non,t,very,\
but,his,nor,than,was,\
by,how,not,that,we,\
can,however,of,the,were,\
could,i,on,their,what,\
d,if,one,them,when"

stop_words = stop_words.split(",")