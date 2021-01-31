from django import template
from pages.models import ProfilePicture, ProfilePictureChosen

register = template.Library()

@register.filter 

def filterProfilePictures(ans, profile_picture_id):

    #Some kind of for loop over the list that takes in the profilePic ID?
    return ans.filter(profile_picture = profile_picture_id)