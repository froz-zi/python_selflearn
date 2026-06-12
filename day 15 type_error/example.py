
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
# >>>