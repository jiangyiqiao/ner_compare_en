#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import nltk
def extract_entity_names(t):
    locs = []
    gpes = []
    orgs = []
    persons =[]
    facilitys = []
    times = []
    moneys = []
    percents = []
    dates = []
    if hasattr(t, 'label') and t.label:  
        #print t.label()
        #print [child[0] for child in t]
        if t.label() == 'GPE':
            gpes.append(' '.join([child[0] for child in t]))
        elif t.label() == 'LOCATION':
            locs.append(' '.join([child[0] for child in t]))
        elif t.label() == 'ORGANIZATION':
            orgs.append(' '.join([child[0] for child in t]))
        elif t.label() == 'PERSON':
            persons.append(' '.join([child[0] for child in t]))
        elif t.label() == 'FACILITY':
            facilitys.append(' '.join([child[0] for child in t]))
        elif t.label() == 'TIME':
            times.append(' '.join([child[0] for child in t]))
        elif t.label() == 'MONEY':
            moneys.append(' '.join([child[0] for child in t]))
        elif t.label() == 'PERCENT':
            percents.append(' '.join([child[0] for child in t]))
        elif t.label() == 'DATE':
            dates.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                ps,os,ls,gs,ts,ms,pers,ds,fs=extract_entity_names(child)
                persons.extend(ps)
                orgs.extend(os)
                gpes.extend(gs)
                locs.extend(ls)
                times.extend(ts)
                moneys.extend(ms)
                percents.extend(pers)
                dates.extend(ds)
                facilitys.extend(fs)
    #return list(set(persons)),list(set(orgs)),list(set(locs)),list(set(gpes)),list(set(times)),list(set(moneys)),list(set(percents)),list(set(datas)),list(set(facilitys))
    return persons,orgs,locs,gpes,times,moneys,percents,dates,facilitys

def nltkner(content):
    sentences = nltk.sent_tokenize(content.strip())
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences,binary=False)
    persons = []
    orgs = []
    locs =[]
    gpes = []
    times = []
    moneys = []
    percents = []
    dates = []
    facilitys = []
    for tree in chunked_sentences:
        person,loc,org,gpe,percent,time,date,money,facility = extract_entity_names(tree)
        persons.extend(person)
        orgs.extend(org)
        gpes.extend(gpe)
        times.extend(time)
        moneys.extend(money)
        percents.extend(percent)
        dates.extend(date)
        facilitys.extend(facility)
    #return list(set(persons)),list(set(locs)),list(set(orgs)),list(set(gpes)),list(set(percents)),list(set(times)),list(set(datas)),list(set(moneys)),list(set(facilitys))
    return persons,locs,orgs,gpes,percents,times,dates,moneys,facilitys
if __name__== '__main__':
    content = """Chinese President Xi Jinping, also general secretary of the Communist Party of China (CPC) Central Committee and chairman of the Central Military Commission, addresses a national conference in Beijing on Tuesday and Wednesday."""
    content_ = """
    Israel, China vow to advance innovation cooperation JERUSALEM, Mar. 30 (Xinhua) -- Israeli and Chinese leaders promised to promote innovation cooperation in various fields, including economy and trade, science and technology, agriculture, health and education, when Israeli Prime Minister Benjamin Netanyahu and President Reuven Rivlin held separate talks this weekwith Chinese Vice Premier Liu Yandong.Israel appreciates that China made the innovation-driven development as a national strategy, said Netanyahu, the prime minister, adding that Israel is willing to strengthen exchanges and become an ideal partner of China in innovation cooperation.Netanyahu said Israel also looks forward to further enhancing cooperation with China in the fields of agriculture, education, science and technology, healthcare, infrastructure and energy, stressing that deepening bilateral pragmatic cooperation is important as such a move is not only consistent with their common strategic interests, but also instrumental in promoting peace and development through the world.China sees Israel as its vital partner, she said, hoping that the two sides will take the second meeting of the joint committee as an opportunity to push forward bilateral innovation cooperation, according to Liu Yandong.Liu stressed the two countries should explore new models of cooperation and make innovation cooperation as a strategic basis for bilateral relations.  Enditem"""
    persons,locs,orgs,gpes,percents,times,dates,moneys,facilitys = nltkner(content)
    
    print 'persons',persons
    print 'locs',locs
    print 'orgs',orgs
    print 'gpes',gpes
    print 'percents',percents
    print 'times',times
    print 'dates',dates
    print 'moneys',moneys
    print 'facilitys',facilitys

    
