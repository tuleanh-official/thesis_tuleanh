from setting import *

def text_to_vector(test_doc):
    test_doc_tfidf = tfidf_vect.transform([test_doc])
    print(np.shape(test_doc_tfidf))
    # test_doc_svd = svd.transform(test_doc_tfidf)

    return test_doc_tfidf