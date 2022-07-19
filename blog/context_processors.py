from . import models


def base_context(request):
    """Function take single argument and return dictonary"""
    all_topics = models.Topic.objects.order_by()
    return {"all_topics": all_topics}
