## 开源英文实体识别结果对比
包括Spacy,NLTK,Standford结果
1. test_nltk.py          #nltk   依赖:import nltk
2. test_stanford.py      #依赖models/.jar models/.gz  修改各jar模型 识别结果相同
3. test_spacy.py         #spacy  依赖：import spacy + en 模型，en模型效果见spacy官网介绍

### 各方法对比结果

* 原句：**__Chinese__** President **__Xi Jinping__**, also general secretary of **__the Communist Party of China (CPC) Central Committee__** and chairman of **__the Central Military Commission__**, addresses a national conference in **__Beijing__** on **__Tuesday and Wednesday__**.


1. NLTK识别结果：

    1. persons
        * Xi Jinping
    2. gpes 
        * Chinese
        * China
        * Beijing


2. 斯坦福ner识别结果：

    1. ORGANIZATION:
        * Communist Party of China (CPC) Central Committee Central
        *  Military Commission
    2. LOCATION
        * Beijing
    3. DATE
        * Tuesday
        * Wednesday

3. Spacy识别结果：

    1. NORP:
        * Chinese
    2. PERSON:
        * Xi Jinping
    3. ORG:
        * the Communist Party of China (CPC) Central Committee
        * the Central Military Commission
    4. GPE:
        * Beijing
    5. DATE:
        * Tuesday and Wednesday


以短句结果足见识别各效果：Spacy 优于 Stanford 优于 NLTK

