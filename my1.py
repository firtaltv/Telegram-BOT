# youtube api key = AIzaSyCQHCskoG-sreYUsKmop2Q9dW0At-ls1bk
# telegram api key = 1720550286:AAGFy8cEUJciLBSESi7uv7QOnxwl6D92ONU
import os
import googleapiclient.discovery
import telebot


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCQHCskoG-sreYUsKmop2Q9dW0At-ls1bk"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet,statistics",
        id="kffacxfA7G4"
    )
    response = request.execute()

    for i in response:
        if i == "items":
            a = response["items"]
            for n in a:
                if "statistics" in n:
                    c = n["statistics"]
                    global k
                    k = ("View Count: " + c["viewCount"] + "\n" + "Likes: " + c["likeCount"] + "\n" + "Dislikes: " + c[
                        "dislikeCount"])
                    return k


print(main())

bot = telebot.TeleBot("1720550286:AAGFy8cEUJciLBSESi7uv7QOnxwl6D92ONU", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, I can show you the clip statistics, especially view / likes / dislikes count. \n"
                          "Write down '/stats' to get it all")


@bot.message_handler(commands=['stats'])
def send_stats(message):
    bot.reply_to(message, main())


# if __name__ == '__main__':
#   main()

bot.polling(none_stop=True, interval=0)
