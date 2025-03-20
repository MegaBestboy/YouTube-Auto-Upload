from pytrends.request import TrendReq
import schedule
import time
import subprocess

def get_trending_topics():
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_searches = pytrends.trending_searches(pn='united_states')
    return trending_searches.head(1).values.flatten().tolist()[0]  # Get top trending topic

def run_pipeline():
    topic = get_trending_topics()
    print(f"🔥 Trending Topic: {topic}")
    subprocess.run(["python", "script_generator.py", topic])  # Pass topic to next step

schedule.every(12).hours.do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)
