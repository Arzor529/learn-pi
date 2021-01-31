from django import template
from pages.models import Quiz, QuizAnswer, QuizQuestion

register = template.Library()

@register.filter 

def filterQuizAnswers(ans, q_id):
    return ans.filter(question = q_id)