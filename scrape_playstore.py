from google_play_scraper import Sort, reviews
import pandas as pd
import time

def scrape_reviews(app_id, total_count=10000):
    all_reviews = []
    count_per_batch = 200  # max per request
    next_token = None

    while len(all_reviews) < total_count:
        result, next_token = reviews(
            app_id,
            lang='id',
            country='id',
            sort=Sort.NEWEST,
            count=count_per_batch,
            continuation_token=next_token
        )
        all_reviews.extend(result)
        print(f"Scraped {len(all_reviews)} reviews...")
        if next_token is None:
            break
        time.sleep(1)  # Delay biar gak diblok

    df = pd.DataFrame(all_reviews)
    df = df[['content', 'score']]
    df = df.rename(columns={'content': 'review', 'score': 'rating'})
    return df

# Contoh penggunaan:
if __name__ == '__main__':
    app_id = 'com.tokopedia.tkpd'  # ID aplikasi di Play Store
    df_reviews = scrape_reviews(app_id, total_count=150000)
    df_reviews.to_csv('tokopedia_reviews.csv', index=False, encoding='utf-8-sig')
    print("Scraping selesai. Data disimpan di 'tokopedia_reviews.csv'")
