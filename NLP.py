from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match(resume, job):
    documents = [resume, job]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    features = vectorizer.get_feature_names_out()

    resume_vec = tfidf_matrix[0].toarray()[0]
    job_vec = tfidf_matrix[1].toarray()[0]

    missing = []

    for i in range(len(features)):
        if job_vec[i] > 0 and resume_vec[i] == 0:
            missing.append(features[i])

    return round(score * 100, 2), missing