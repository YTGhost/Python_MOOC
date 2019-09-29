import jieba

s = "中国是一个伟大的国家"
print(jieba.lcut(s))  # 精确模式，返回一个列表类型的分词结果
print(jieba.lcut(s, cut_all=True))  # 全模式，返回一个列表类型的分词结果，存在冗杂。
print(jieba.lcut_for_search("中华人民共和国是伟大的"))  # 搜索引擎模式，返回一个列表类型的分词结果，存在冗杂。
# jieba.add_word(w)     向分词词典增加新词w
