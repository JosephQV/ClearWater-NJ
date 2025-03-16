from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import feedparser
import time
from datetime import datetime, timedelta
import webbrowser

from shared_config import NEWS_SITES, NEWS_KEY_WORDS, IMAGES


def get_recent_news(topic):
    if topic == "general":
        # 1. NJ Future news feed
        nj_future_feed = feedparser.parse(NEWS_SITES["en"]["nj_future"])
        nj_future_articles = []
            
        for entry in nj_future_feed.entries[:10]:  # Get the latest 10 articles
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
            # Check if article is recent enough to consider
            if check_date_is_recent(entry.published_parsed, max_days_old=90):
                # Check if the tags associated with the article fit at least 1 desired keyword
                tags = [tag["term"] for tag in entry.tags]
                count = 0
                threshold = 1
                for tag in tags:
                    if tag.lower() in NEWS_KEY_WORDS:
                        count += 1
                    if count == threshold:
                        nj_future_articles.append(article)
                        break
        
        # 2. NJDEP News Releases
        njdep_articles = []
        njdep_feed = feedparser.parse(NEWS_SITES["en"]["njdep"])
            
        for entry in njdep_feed.entries[:10]:  # Get the latest 10 articles
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
            # Check if article is recent enough to consider
            if check_date_is_recent(entry.published_parsed, max_days_old=90):
                # Check if the tags associated with the article fit at least 1 desired keyword
                tags = entry.title.lower().split() + entry.summary.lower().split()
                count = 0
                threshold = 1
                for tag in tags:
                    if tag in NEWS_KEY_WORDS:
                        count += 1
                    if count == threshold:
                        nj_future_articles.append(article)
                        break
    
        # Combine and sort by published date
        news_articles = nj_future_articles + njdep_articles
        # Return sorted dictionary of relevant articles
        return news_articles
    
    elif topic == "my_water_system":
        water_system_feed = feedparser.parse(NEWS_SITES["en"]["nj_american_water"])
        water_system_articles = []
            
        for entry in water_system_feed.entries[:10]:  # Get the latest 10 articles
            print(entry)
            article = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published[:17],
                "summary": entry.summary,
                "img_source": IMAGES["nj_american_water"]
            }
            # Check if article is recent enough to consider
            if check_date_is_recent(entry.published_parsed, max_days_old=90):
                water_system_articles.append(article)
        
        return water_system_articles
    

def check_date_is_recent(struct_time_obj, max_days_old):
    # Convert struct_time to datetime
    dt_obj = datetime.fromtimestamp(time.mktime(struct_time_obj))
    
    # Calculate the date 3 months ago (approximate as 90 days)
    three_months_ago = datetime.now() - timedelta(days=max_days_old)
    
    return dt_obj >= three_months_ago



class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.load_app, 5)
        
    def load_app(self, instance):
        self.manager.switch_screens("home_screen", "fade")
        
        
class WaterNewsFeed(BoxLayout):
    pass


class ArticleList(GridLayout):
    topic = StringProperty("")
    
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.add_news_articles)
        
    def add_news_articles(self, instance):
        news_articles = get_recent_news(self.topic)
        
        for article in news_articles:
            self.add_widget(
                NewsItem(
                    title=article["title"],
                    link=article["link"],
                    published=article["published"],
                    summary=article["summary"],
                    img_source=article["img_source"]
                )
            )
        


class NewsItem(BoxLayout):
    title = StringProperty("")
    link = StringProperty("")
    published = StringProperty("")
    summary = StringProperty("")
    img_source = StringProperty("")
    
    def __init__(
        self,
        title,
        link,
        published,
        summary,
        img_source, 
        **kw
    ):
        super().__init__(**kw)
        self.title = title
        self.link = link
        self.published = published
        self.summary = summary
        self.img_source = img_source
        
    def open_news_link(self):
        if self.link is not None:
            webbrowser.open(self.link)