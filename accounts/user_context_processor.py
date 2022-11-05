from .models import Profile


def get_profile(request):
    if request.user.is_authentecated:
        profile = Profile.objects.get(user=request.user)
        return{'user_profile':profile}
    else:
        return {}
