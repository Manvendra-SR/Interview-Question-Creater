prompt_template = """
You are an expert at creating questions based on study materials, presentations, and documentation.
Your goal is to prepare a student or presenter for their exams, interviews, or talks.

------------
{text}
------------

Create exactly 5 questions.
Do not include explanations, reasons, or extra notes.
Output must only be in the following format (no blank lines between questions):

1) [Question 1]
2) [Question 2]
3) [Question 3]
4) [Question 4]
5) [Question 5]

QUESTIONS:
"""

refine_template = ("""
You are an expert at creating and refining practice questions based on study material, presentations, or documentation.
Your goal is to help a student or presenter prepare for exams, interviews, or talks.
We already have some practice questions to a certain extent: {existing_answer}.
You may refine the existing questions or add new ones (only if necessary) using the additional context below.

------------
{text}
------------

Given the new context, refine the original questions in clear English.
If the context does not add value, please provide the original questions.
Provide exactly 5 questions.
Do not include explanations, reasons, or extra notes.
Output must only be in the following format (no blank lines between questions):

1) [Question 1]
2) [Question 2]
3) [Question 3]
4) [Question 4]
5) [Question 5]

QUESTIONS:
"""
)
