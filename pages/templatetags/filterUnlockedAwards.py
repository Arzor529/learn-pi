from django import template
from pages.models import Award, AwardUnlocked

register = template.Library()

@register.filter 

def filterUnlockedAwards(ans, award_id):
    return ans.filter(award = award_id)