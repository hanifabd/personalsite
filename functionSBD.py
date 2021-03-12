from pickle import load
import re

def sent_segment_svc(artic):
    movec = load(open('model/sentence_boundary_disambiguation/vectorizer_model.sav','rb'))
    model = load(open('model/sentence_boundary_disambiguation/sbd_model.sav','rb'))
    artic = re.findall(r"[\w']+|[.,!?;]", artic)
    null_tags = [(token, 'NULL') for token in artic]
    input = [get_feature(null_tags[i][0], null_tags[i][1],i, null_tags) for i in range(len(null_tags))]
    X_artic = movec.transform(input)
    y_artic = model.predict(X_artic)
    result = print_sentences(artic, y_artic)
    return result

def get_feature(token, tag,token_index, sent):
    token_feature = {
      'bias'                  : 1.0,

      'init.token.digit'       : token.isdigit(),
      'init.token.capsInside'  : token[1:].lower() != token[1:],

      'init.token[3:]'         : '' if len(token) < 3  else token[:3],
      'init.token[2:]'         : '' if len(token) < 2  else token[:2],
      'init.token[-3:]'        : '' if len(token) < 3  else token[-3:],
      'init.token[-2:]'        : '' if len(token) < 2  else token[-2:],
      
      'init.token.lower'       : token.lower(),
      'init.token.title'       : token.istitle(),
      'init.token.upper'       : token.isupper(),
      
      'prev.token.lower'       : '' if token_index == 0     else sent[token_index - 1][0].lower(),
      'prev.token.title'       : '' if token_index == 0     else sent[token_index - 1][0].istitle(),
      'prev.token.upper'       : '' if token_index == 0     else sent[token_index - 1][0].isupper(),
      
      'next.token.lower'       : '' if token_index == len(sent) - 1     else sent[token_index + 1][0].lower(),
      'next.token.title'       : '' if token_index == len(sent) - 1     else sent[token_index + 1][0].istitle(),
      'next.token.upper'       : '' if token_index == len(sent) - 1     else sent[token_index + 1][0].isupper(),
    }
    return token_feature

def print_sentences(artic, y_artic):
    corpus = []
    corp = []
    for i,word in enumerate(list(zip(artic, y_artic))):
        if (word[1] == '1'):
            if corp != []:
                corpus.append(corp)
                corp = []
            corp.append(word[0])
        elif (i == (len(artic)-1)):
            if corp != []:
                corp.append(word[0])
                corpus.append(corp)
                corp = []
        else:
            corp.append(word[0])

    sentences = []
    for sentence in corpus:
        sentence = ' '.join(sentence)
        sentences.append(sentence)
    return sentences