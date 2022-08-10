import sys

if __name__ == '__main__':
    news = [line.strip() for line in sys.stdin]
    topic = news[-1]
    my_news = [tuple(line.split(' / ')) for line in news[:-1]]
    my_news.sort(key=lambda x: (float(x[2]), x[0]))
    for line in my_news:
        if line[1] == topic:
            print(line[0])