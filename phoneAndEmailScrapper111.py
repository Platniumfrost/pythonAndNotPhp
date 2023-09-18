import re, pyperclip


re.compile(r'''
# 415-55-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext.12345, x12345

((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext\.)?\s) |x)   #extension word-part (optional)
  (\d{2,5}))?   # extension number-part (optional)
''', re.VERBOSE)

re.compile('((\d\d\d) | (\(\d\d\d)))?(\d|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}
