# ============================================================
# TRIE (PREFIX TREE) - PATTERN TEMPLATE
# ============================================================
#
# A trie is a tree structure where each node represents a character.
# Paths from root to nodes form prefixes of stored strings.
# Used for efficient prefix-based searching.
#
# NODE STRUCTURE:
#   class TrieNode:
#       def __init__(self):
#           self.children = {}   # char → TrieNode
#           self.is_end = False  # marks end of a complete word
#
# OPERATIONS:
#
#   Insert word:
#       Traverse char by char, creating nodes as needed.
#       Mark the last node as is_end = True.
#
#   Search word:
#       Traverse char by char. If any char missing → False.
#       At end, check is_end == True.
#
#   Starts with (prefix search):
#       Same as search but don't check is_end.
#
# WHEN TO USE:
#   - Autocomplete / prefix matching
#   - Word search in grid
#   - Spell checking
#   - IP routing (longest prefix match)
#   - Counting words with a given prefix
#
# TIME: O(m) per operation where m = word/prefix length
# SPACE: O(total characters across all words)
# ============================================================
