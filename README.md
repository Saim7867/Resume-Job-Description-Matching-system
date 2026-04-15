# Resume-Job-Description-Matching-system
Simple AI matcher that compares a resume with a job description to see how well they match. The goal is to see how well an applicant's resume matches with a job posting. Explores NLP - natural language processing technqiues and how they can apply in the real world Many resumes are filtered out by applicant tracking systems, this tool will help users understand how closely their resume may match with a job description

HOW IT WORKS: the resume and job description are taken as text input (in this case pre-written) and both texts are converted into numerical representations using their term frequency. Cosine simmilarity is used to determine how closely the two texts match.

TOOLS IN USE: 
Python 
SickitLearn (TF IDF, cosine simmilarity) 
NumPy
