from collections import defaultdict


def best_sender(messages: list, senders: list):
    result = defaultdict(int)
    for i, name in enumerate(senders):
        result[name] += len(messages[i].split())
    return max([(k, v) for k, v in result.items()], key=lambda x: (x[1], x[0]))[0]


if __name__ == '__main__':
    messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
    senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

    print(best_sender(messages, senders))
