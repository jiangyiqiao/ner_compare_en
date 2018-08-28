#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import spacy
def test_spacyner(text):
    nlp = spacy.load('en_core_web_sm')
    ner_content = nlp(unicode(text))
    for i in range(0,len(ner_content)):
        #print ner_content[i].text,ner_content[i].ent_iob_,ner_content[i].ent_type_
        if ner_content[i].ent_type_ != 'O' and ner_content[i].ent_iob_ != 'O':
            print ner_content[i].text,ner_content[i].ent_iob_,ner_content[i].ent_type_
if __name__=='__main__':
    text = """Chinese President Xi Jinping, also general secretary of the Communist Party of China (CPC) Central Committee and chairman of the Central Military Commission, addresses a national conference in Beijing on Tuesday and Wednesday."""
    text_ = """Israel, China vow to advance innovation cooperation JERUSALEM, Mar. 30 (Xinhua) -- Israeli and Chinese leaders promised to promote innovation cooperation in various fields, including economy and trade, science and technology, agriculture, health and education, when Israeli Prime Minister Benjamin Netanyahu and President Reuven Rivlin held separate talks this weekwith Chinese Vice Premier Liu Yandong.Israel appreciates that China made the innovation-driven development as a national strategy, said Netanyahu, the prime minister, adding that Israel is willing to strengthen exchanges and become an ideal partner of China in innovation cooperation.Netanyahu said Israel also looks forward to further enhancing cooperation with China in the fields of agriculture, education, science and technology, healthcare, infrastructure and energy, stressing that deepening bilateral pragmatic cooperation is important as such a move is not only consistent with their common strategic interests, but also instrumental in promoting peace and development through the world.China sees Israel as its vital partner, she said, hoping that the two sides will take the second meeting of the joint committee as an opportunity to push forward bilateral innovation cooperation, according to Liu Yandong.Liu stressed the two countries should explore new models of cooperation and make innovation cooperation as a strategic basis for bilateral relations.  Enditem
    """
    test_spacyner(text)
