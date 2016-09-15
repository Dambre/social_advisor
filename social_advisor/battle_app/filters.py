import enchant
import nltk; nltk.data.path.append('nltk_data')

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
TYPES = (
	'NN', 'NNS',
	'RB', 'RBR', 'RBS',
	'JJ', 'JJR', 'JJS',
	'VB')

tagdict = nltk.data.load('help/tagsets/upenn_tagset.pickle')
TYPES_DESC = [(_type, tagdict[_type][0]) for _type in TYPES]

#exclude words with prefixes or parts in words e.g http://word.com
EXCLUDE_WORDPARTS = ('http://', '//', 'https://', 'HTTP://', 'HTTPS://')
