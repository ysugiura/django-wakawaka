from django.conf import settings

LOCK_CACHE_PREFIX = getattr(settings, "WAKAWAKA_LOCK_CACHE_PREFIX", "wwl")

LOCK_TIMEOUT = getattr(settings, "WAKAWAKA_LOCK_TIMEOUT", 60*60)

DEFAULT_INDEX = getattr(settings, 'WAKAWAKA_DEFAULT_INDEX', 'WikiIndex')

# Default Wiki word is in [[wikiword]] format.
WIKI_SLUG = r'\[\[(.*?)\]\]'
WIKI_SLUG = getattr(settings, 'WAKAWAKA_SLUG_REGEX', WIKI_SLUG)
