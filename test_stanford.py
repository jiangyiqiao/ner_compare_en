#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from nltk.tag import StanfordNERTagger

if __name__=='__main__':
    jar = 'models/stanford-ner.jar'
    #jar = 'models/stanford-ner-3.9.1-javadoc.jar'
    #jar = 'models/stanford-ner-3.9.1-sources.jar'
    model = 'models/english.muc.7class.distsim.crf.ser.gz'
    st = StanfordNERTagger(model,jar)
    text = """Chinese President Xi Jinping, also general secretary of the Communist Party of China (CPC) Central Committee and chairman of the Central Military Commission, addresses a national conference in Beijing on Tuesday and Wednesday."""
    text_ = """Israel, China vow to advance innovation cooperation JERUSALEM, Mar. 30 (Xinhua) -- Israeli and Chinese leaders promised to promote innovation cooperation in various fields, including economy and trade, science and technology, agriculture, health and education, when Israeli Prime Minister Benjamin Netanyahu and President Reuven Rivlin held separate talks this weekwith Chinese Vice Premier Liu Yandong.Israel appreciates that China made the innovation-driven development as a national strategy, said Netanyahu, the prime minister, adding that Israel is willing to strengthen exchanges and become an ideal partner of China in innovation cooperation.Netanyahu said Israel also looks forward to further enhancing cooperation with China in the fields of agriculture, education, science and technology, healthcare, infrastructure and energy, stressing that deepening bilateral pragmatic cooperation is important as such a move is not only consistent with their common strategic interests, but also instrumental in promoting peace and development through the world.China sees Israel as its vital partner, she said, hoping that the two sides will take the second meeting of the joint committee as an opportunity to push forward bilateral innovation cooperation, according to Liu Yandong.Liu stressed the two countries should explore new models of cooperation and make innovation cooperation as a strategic basis for bilateral relations.  Enditem
    """
    ner_contents = st.tag(text.split())
    for ner_content in ner_contents:
        #print ner_content[0],ner_content[1]
        if ner_content[1] != 'O':
            print ner_content[0],ner_content[1]


