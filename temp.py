# -*- coding: utf-8 -*-
import json,collections
words = ["kama", "mimi", "yake", "kwamba", "yeye", "mara", "kwa", "juu ya", "wako", "kwa", "wao", "kuwa", "katika", "moja", "na", "hii", "kutoka", "na", "moto","neno", "lakini", "nini", "baadhi", "ni", "yake", "ninyi", "au", "alikuwa", "akaonekana", "ya", "kwa", "na", "a", "katika", "sisi", "unaweza", "nje", "nyingine", "walikuwa", "ambayo", "kufanya", "yao", "wakati", "kama", "mapenzi", "jinsi", "alisema", "an", "kila", "kuwaambia", "gani", "kuweka", "tatu", "wanataka", "hewa", "vizuri", "pia", "kucheza", "ndogo", "mwisho", "kuweka", "nyumbani", "kusoma", "mkono", "bandari", "kubwa", "Spell", "kuongeza", "hata", "ardhi", "hapa", "lazima", "kubwa", "high", "kama", "kufuata", "tendo", "kwa nini","kuuliza", "wanaume", "mabadiliko ya", "akaenda", "mwanga", "aina", "mbali", "haja", "nyumba", "picha", "kujaribu", "sisi", "tena", "mnyama", "uhakika", "mama", "dunia", "karibu", "kujenga", "binafsi", "dunia", "baba", "yoyote", "mpya", "kazi", "sehemu", "kuchukua", "kupata", "mahali", "alifanya", "kuishi", "ambapo", "baada ya", "nyuma", "kidogo", "tu", "pande zote", "mtu", "mwaka", "alikuja", "Onyesha", "kila", "nzuri", "mimi", "kutoa", "wetu", "chini ya", "jina", "sana", "kupitia", "tu", "aina", "hukumu", "kubwa", "kufikiri", "kusema", "msaada", "chini", "line", "tofauti", "upande", "sababu", "kiasi","maana", "kabla ya", "hoja", "haki", "mvulana", "umri wa", "pia", "sawa", "yeye", "kila", "huko", "wakati", "up", "kutumia", "yako", "njia","kuhusu", "wengi", "kisha", "yao", "kuandika", "ingekuwa", "kama", "hivyo", "haya", "yake", "muda mrefu", "kufanya", "kitu", "kuona", "naye","mbili", "ina", "kuangalia", "zaidi", "siku", "inaweza", "kwenda", "kuja", "alifanya", "simu", "sauti", "hakuna", "zaidi", "watu", "yangu", "juu ya", "kujua", "maji", "kuliko", "simu", "kwanza", "ambao", "inaweza", "chini", "upande", "imekuwa", "sasa","kupata", "kichwa", "kusimama", "mwenyewe", "ukurasa", "lazima", "nchi", "kupatikana", "jibu", "shule", "kukua", "utafiti", "bado", "kujifunza", "kupanda", "cover", "chakula", "jua", "nne", "kati ya", "hali", "kuweka", "jicho","kamwe", "mwisho", "basi", "wazo", "mji", "ya mti", "msalaba", "shamba", "ngumu", "kuanza", "nguvu", "hadithi", "saw", "mbali", "bahari", "kuteka","kushoto", "marehemu", "kukimbia", "kufanya si", "wakati", "vyombo vya habari", "karibu", "usiku", "halisi", "maisha", "chache", "kaskazini", "kitabu", "kubeba", "alichukua", "sayansi", "kula", "chumba", "rafiki", "alianza","wazo", "samaki", "mlima", "kuacha", "mara moja", "msingi", "kusikia", "farasi", "kata", "uhakika", "kuangalia", "rangi", "uso", "mbao","kuu", "wazi", "wanaonekana", "pamoja", "ijayo", "nyeupe", "watoto", "kuanza", "got", "kutembea", "mfano", "kupunguza", "karatasi", "kundi", "daima", "muziki","wale", "wote wawili", "alama", "mara nyingi", "barua", "mpaka", "maili", "mto", "gari", "miguu", "huduma", "pili", "kutosha", "wazi", "msichana","kawaida", "vijana", "tayari", "juu", "milele", "nyekundu", "orodha", "ingawa", "kujisikia", "majadiliano", "ndege", "hivi karibuni", "mwili", "mbwa", "familia","moja kwa moja", "litasababisha", "kuondoka", "wimbo", "kupima", "mlango", "bidhaa", "nyeusi", "mfupi", "numeral", "darasa", "upepo", "swali", "kutokea", "kamili", "meli", "eneo", "nusu", "mwamba", "ili","moto", "kusini", "tatizo", "kipande", "aliiambia", "alijua", "kupita", "tangu", "juu", "zima", "mfalme", "mitaani", "inchi", "kuzidisha", "chochote", "Bila shaka", "kukaa", "gurudumu", "full", "nguvu", "bluu", "kitu", "kuamua", "uso", "kina", "mwezi","kisiwa", "mguu", "mfumo", "busy", "mtihani", "rekodi", "mashua", "kawaida", "dhahabu", "iwezekanavyo", "ndege", "badala", "kavu", "ajabu", "kucheka", "elfu", "iliyopita", "mbio", "kuangalia", "mchezo", "sura","wanalinganisha", "moto", "miss ya", "kuletwa", "joto", "theluji", "tairi", "kuleta", "ndiyo", "mbali", "kujaza", "mashariki", "rangi", "lugha", "kati ya", "kitengo", "nguvu", "mji", "faini", "baadhi ya", "kuruka", "kuanguka", "kusababisha", "kilio", "giza", "mashine", "note", "kusubiri", "mpango", "takwimu","nyota", "sanduku", "nomino", "shamba", "wengine", "sahihi", "uwezo", "chupa", "kutenda", "uzuri", "gari", "alisimama", "vyenye", "mbele", "kufundisha", "wiki", "mwisho", "alitoa", "kijani", "oh", "haraka", "kuendeleza", "bahari", "joto", "bure", "dakika", "nguvu", "maalum", "akili", "nyuma ya", "wazi", "mkia", "kuzalisha", "ukweli", "nafasi","habari", "bora", "saa", "bora", "kweli", "wakati wa", "mia", "tano", "kumbuka", "hatua", "mapema", "kushikilia", "magharibi", "ardhi", "maslahi", "kufikia", "haraka", "kitenzi", "kuimba", "kusikiliza", "sita", "meza", "usafiri", "chini ya", "asubuhi", "kumi", "rahisi", "kadhaa", "vowel", "kuelekea", "vita","kuweka", "dhidi ya", "muundo", "polepole", "kituo cha", "upendo", "mtu", "fedha", "kutumika", "itaonekana", "barabara", "ramani", "mvua", "utawala", "serikali", "kuvuta", "baridi","ilani", "sauti", "nishati", "kuwinda", "kinachowezekana", "kitanda", "ndugu", "yai", "safari", "kiini", "amini", "labda", "kuchukua", "ghafla", "kuhesabu", "mraba", "sababu", "urefu", "kuwakilisha","sanaa", "somo", "kanda", "ukubwa", "kutofautiana", "kuishi", "kusema", "uzito", "ujumla", "barafu", "jambo", "mzunguko", "jozi", "ni pamoja na", "mgawanyiko", "silabi", "waliona", "kuu", "mpira", "bado", "wimbi", "kuacha", "moyo", "ni", "sasa", "nzito", "ngoma", "injini", "nafasi", "mkono", "pana", "meli", "vifaa", "sehemu", "msitu", "kukaa", "mbio", "dirisha", "kuhifadhi","majira ya joto", "treni", "usingizi", "kuthibitisha", "ya lone", "mguu", "zoezi", "ukuta", "kukamata", "mlima", "unataka", "anga", "bodi", "furaha", "majira ya baridi", "ameketi", "imeandikwa", "pori", "chombo", "naendelea", "kioo", "nyasi", "ng’ombe", "kazi", "makali", "ishara", "ziara", "siku za nyuma", "laini", "furaha", "mkali", "gesi", "hali ya hewa", "mwezi", "milioni", "kubeba", "kumaliza", "furaha", "matumaini", "ua", "nguo", "ajabu", "kuondoka", "biashara", "kuimba", "safari", "ofisi", "kupokea", "mstari", "kinywa", "halisi", "ishara", "kufa", "angalau", "shida", "kelele", "ila", "aliandika", "mbegu", "tone", "kujiunga na", "kupendekeza","safi", "mapumziko", "mwanamke", "yadi", "kupanda", "mbaya", "pigo", "mafuta", "damu", "kugusa", "ilikua", "cent", "kuchanganya", "timu", "waya", "gharama", "waliopotea", "kahawia", "kuvaa", "bustani", "sawa", "alimtuma", "kuchagua", "akaanguka", "fit", "kati yake", "haki", "benki", "kukusanya", "kuokoa", "kudhibiti", "decimal", "sikio", "mwingine", "kabisa", "kuvunja", "kesi", "katikati", "kuua", "mwana", "ziwa", "wakati", "wadogo", "kubwa", "chemchemi", "kuchunguza", "mtoto", "moja kwa moja", "consonant", "taifa", "kamusi", "maziwa", "kasi", "njia", "chombo", "kulipa", "umri", "sehemu", "mavazi", "wingu", "mshangao", "utulivu", "jiwe", "vidogo", "kupanda", "baridi", "kubuni", "maskini", "mengi", "majaribio", "chini", "ufunguo", "chuma", "moja", "fimbo", "gorofa", "ishirini", "ngozi", "tabasamu", "na crease", "shimo", "kuruka", "mtoto", "nane", "kijiji", "kukutana", "mizizi", "kununua", "kuongeza", "kutatua", "chuma", "kama", "kushinikiza", "saba","aya", "tatu", "atakuwa", "uliofanyika", "nywele", "kuelezea", "mpishi", "sakafu", "ama", "matokeo", "kuchoma", "kilima", "salama", "paka", "karne ya", "kufikiria", "aina", "sheria", "kidogo", "pwani", "nakala", "maneno", "kimya", "mrefu", "mchanga", "udongo", "orodha", "joto", "kidole", "sekta ya", "thamani", "kupambana", "uongo", "kuwapiga", "kuchochea", "asili", "mtazamo", "maana", "mji mkuu wa", "si", "kiti", "hatari", "matunda", "tajiri", "nene", "askari", "mchakato", "kazi", "mazoezi", "tofauti", "vigumu", "daktari", "tafadhali", "kulinda", "saa sita mchana", "mazao", "kisasa", "kipengele", "hit", "mwanafunzi", "kona", "chama", "usambazaji", "ambao", "Machapisho", "pete", "tabia ya", "wadudu", "hawakupata", "kipindi", "zinaonyesha", "za Redio", "alizungumza", "chembe", "binadamu", "historia", "athari", "umeme", "kutarajia", "mfupa", "reli", "kufikiria", "kutoa", "kukubaliana", "hivyo", "mpole", "mwanamke","nahodha", "nadhani", "muhimu", "mkali", "mrengo", "kujenga", "jirani", "osha", "bat kwa", "badala", "umati wa watu", "nafaka", "kulinganisha", "shairi", "kamba", "kengele", "hutegemea", "nyama", "kusugua", "tube", "maarufu", "dola", "mkondo", "hofu", "mbele", "nyembamba", "pembetatu", "sayari", "haraka", "wakuu", "koloni", "saa", "yangu", "tie", "kuingia", "kuu", "safi", "search", "kutuma", "njano", "bunduki", "kuruhusu", "magazeti", "wafu", "doa", "jangwa", "suti", "sasa", "kuinua", "kufufuka", "kuwasili", "bwana", "kufuatilia", "mzazi", "pwani", "mgawanyiko", "karatasi", "Dutu", "neema", "kuungana", "baada", "kutumia", "gumzo", "mafuta", "furaha", "awali", "kushiriki", "kituo cha", "baba", "mkate", "malipo", "sahihi", "bar ya", "kutoa", "sehemu", "mtumwa", "bata", "papo", "soko", "shahada ya", "idadi ya", "kifaranga", "wapenzi", "adui", "jibu","kunywa","kutokea","msaada","hotuba","asili","mbalimbali","mvuke","mwendo","njia","kioevu","kuingia","maana","quotient ya","meno","ganda","shingo","oksijeni","sukari","kifo","wa pretty","ujuzi","wanawake","msimu","ufumbuzi","sumaku","fedha","kuwashukuru","tawi","mechi","suffix","hasa","mtini","hofu","kubwa","dada","chuma","kujadili","mbele","sawa","kuongoza","uzoefu","alama","mboni","kununuliwa","kuongozwa","lami","kanzu","habari","kadi","bendi","kamba","kuingizwa","kushinda","ndoto","jioni","hali","kulisha","chombo","jumla","msingi","harufu","bonde","wala","mara mbili","kiti cha","kuendelea","kuzuia","chati","kofia","kuuza","mafanikio","kampuni","Ondoa","tukio","hasa","mpango","kuogelea","mrefu","kinyume","mke","kiatu","bega","kuenea","kupanga","kambi","mzulia","pamba","aliyezaliwa","kuamua","lita moja","tisa","lori","kelele","ngazi ya","nafasi","kukusanya","duka","kunyoosha","kutupa","uangaze","mali","safu","molekuli","kuchagua","makosa","kijivu","kurudia","zinahitaji","pana","kuandaa","chumvi","pua","wingi","hasira","madai","bara"]
hindi = ["में","है","हैं","नहीं","लिए","गया","तथा","अपने","कुछ","साथ","होता","था","दिया","हुए","कोई","रूप","से","मैं","रहा","हुआ","बात","कहा","समय","क्या","अपनी","होती","प्रकार","बहुत","तरह","बाद","फिर","रहे","द्वारा","अधिक","रही","होने","एवं","हुई","थे","उनके","थी","वाले","चाहिए","दिन","लेकिन","काम","हूँ","होते","इसके","उन्हें","गये","कभी","आदि","लोग","बार","यहाँ","दोनों","उन्होंने","कार्य","पास","वहाँ","भारत","लिया","प्राप्त","उनकी","लोगों","गयी","लगा","अन्य","होगा","इसी","देश","यदि","सभी","नाम","वर्ष","ऐसा","विकास","अपना","ऐसे","दूसरे","हाथ","भाषा","मेरे","मैंने","तुम","बीच","वाली","बड़े","प्रति","व्यक्ति","उनका","लिये","इसलिए","तीन","इसका","ऐसी","विशेष","बड़ी","अथवा"]

word_lengths = collections.defaultdict(list)

for w in hindi:
    ascii = True
    for c in w:
        if ord(c) > 127:
            # ascii = False
            print ord(c),c
    if ascii:
        word_lengths[len(w)].append(w)

for length,word_list in word_lengths.items():
    print length, len(word_list)

json.dump(word_lengths,open('hindi.json','w'))
