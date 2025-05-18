import feedparser
import time
from datetime import datetime, timedelta
import webbrowser

from data.app_config import IMAGES
from data.news_config import NEWS_SITES, NEWS_KEY_WORDS


class HomeController:
    def __init__(self):
        self.feeds = NEWS_SITES
        
    def get_recent_news(self, topic):
        all_articles = []
        for source_name, feed_link in self.feeds[topic]:
            feed = feedparser.parse(feed_link)
            feed_articles = []
            
            for entry in feed.entries[:10]:
                # Check if article is recent enough to consider
                if self.check_date_is_recent(entry.published_parsed, max_days_old=90):
                    # Check if the tags associated with the article fit at least 1 desired keyword
                    if self.check_for_relevant_tags():
                        article = self.process_article(entry, source_name)
                        feed_articles.append(article)
            all_articles.append(feed_articles)
        return all_articles
            
    def process_article(self, entry, source_name):
        if source_name == "nj_future":
            article = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published[:17],
                "summary": entry.summary,
                "img_source": IMAGES["njfuture"]
            }
            # Remove a part of the summary string that is not wanted
            s =  article["summary"]
            s = s.replace("<p>", "")
            s = s.replace("</p>", "")
            index = s.find("The post")
            article["summary"] = s[:index].strip() if index != -1 else s
            
            return article
        elif source_name == "njdep":
            article = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published[:17],
                "summary": entry.summary,
                "img_source": IMAGES["njdep"]
            }
            # Remove a part of the summary string that is not wanted
            s =  article["summary"]
            s = s.replace("<p>", "")
            s = s.replace("</p>", "")
            index = s.find("/>")
            article["summary"] = s[index+2:].strip() if index != -1 else s
            
            return article
        elif source_name == "nj_american_water":
            article = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published[:17],
                "summary": entry.summary,
                "img_source": IMAGES["nj_american_water"]
            }
            return article

    def check_date_is_recent(self, struct_time_obj, max_days_old):
        # Convert struct_time to datetime
        dt_obj = datetime.fromtimestamp(time.mktime(struct_time_obj))
        
        # Calculate the date 3 months ago (approximate as 90 days)
        three_months_ago = datetime.now() - timedelta(days=max_days_old)
        
        return dt_obj >= three_months_ago
    
    def check_for_relevant_tags(self, feed_entry):
        tags = [tag["term"] for tag in feed_entry.tags]
        count = 0
        threshold = 1
        for tag in tags:
            if tag.lower() in NEWS_KEY_WORDS:
                count += 1
            if count == threshold:
                return True
        return False