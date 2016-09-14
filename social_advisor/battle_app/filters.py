import enchant

en_US = enchant.Dict('en_US')
en_GB = enchant.Dict('en_GB')

AVAILABLE_LANGUAGES = (en_US, en_GB)

# TYPES is used
# exluded word types .
EXCLUDE_TYPES = ('$', "''", '(', ')', ',',
    '--', '.', ':', 'CC', 'CD', 'DT', 'EX',
    'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS',
    'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'SYM', 'TO')

# TYPES - tuple of required word type e.g. "NN" - noun etc.
TYPES = ('NN', 'ADV', 'ADJ')

#exclude words with prefixes or parts in words e.g http://word.com
EXCLUDE_WORDPARTS = ('http://', '//', 'https://', 'HTTP://', 'HTTPS://')
