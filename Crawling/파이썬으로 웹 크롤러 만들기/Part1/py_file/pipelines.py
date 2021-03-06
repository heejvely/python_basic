from datetime import datetime
from items import Article
from string import whitespace

class WikispiderPipeline(object):
    def process_item(self, article, spider):
        dateStr = article['lastUpdated']
        dateStr = dateStr.replace('This page was last edited on', '')
        dateStr = dateStr.strip()
        dateStr = datetime.strptime(dateStr, '%d %B %Y, at %H:%M.')
        dateStr = dateStr.strftime('%Y-%m-%d %H:%M:%S')
        article['lastUpdated'] = dateStr
        
        texts = article['text'][0:50]
        texts = [line for line in texts if line not in whitespace]
        article['text'] = ''.join(texts)
        return article