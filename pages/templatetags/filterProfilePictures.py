from django import template
from pages.models import ProfilePicture, ProfilePictureChosen

register = template.Library()

@register.filter 

def filterProfilePictures(ans, profile_picture_id):
    return ans.filter(profile_picture = profile_picture_id)