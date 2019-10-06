import wordcloud

w = wordcloud.WordCloud()
w.generate("Python and WordCloud")
w.to_file("outfile.png")
