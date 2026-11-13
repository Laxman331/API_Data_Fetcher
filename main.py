
import requests
import json


def fetch_posts():

    url = "https://jsonplaceholder.typicode.com/posts"

    page = 1
    all_posts = []

    while True:

        params = {
            "_page": page,
            "_limit": 10
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Unexpected API response format")

        if len(data) == 0:
            break

        all_posts.extend(data)

        print("Page:", page, "| Records:", len(data))

        page += 1

    return all_posts


def save_posts(posts):

    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)

    print("Posts saved successfully in JSON file")


def load_posts():

    with open("posts.json", "r", encoding="utf-8") as file:
        total_posts = json.load(file)

    return total_posts


def main():

    try:
        posts = fetch_posts()

        print("Total fetched records:", len(posts))

        save_posts(posts)

        all_posts = load_posts()

        print("Total records in JSON file:", len(all_posts))

        if all_posts:
            print("First post title:", all_posts[0]["title"])
            print("Last post ID:", all_posts[-1]["id"])
        else:
            print("No posts available.")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    except (ValueError, OSError) as e:
        print("Data or file processing error:", e)


if __name__ == "__main__":
    main()
