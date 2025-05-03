def friend_of_friend(user_id, users_friendship_dataset: list):
    """
    find friends of a friend.
    :param user_id: friend_id
    :param users_friendship_dataset: list of users friendship dataset
    :return: list | a list of input user id friends
    """
    return [foaf_id for friend_id in users_friendship_dataset[user_id['id']] for foaf_id in users_friendship_dataset[friend_id]]


def find_mutual_friends_total(user_id, friend_id, users_friendship_dataset: list):
    """

    :param user_id:
    :param friend_id:
    :param users_friendship_dataset:
    :return:
    """


def find_best_suggestion(users_dataset: list, user_id: int):
    """
    find the best suggestion for user.
    :param users_dataset:
    :param user_id:
    :return:
    """





if __name__ == '__main__':
    users_dataset = [{'id': 0, 'name': 'hadise', 'friends': [1, 2, 4]},
                     {'id': 1, 'name': 'sogand', 'friends': [0, 2, 4]},
                     {'id': 2, 'name': 'aynaz', 'friends': [0, 1, 4]},
                     {'id': 3, 'name': 'amin', 'friends': [4, 5, 7]},
                     {'id': 4, 'name': 'mahdi', 'friends': [0, 1, 2, 3, 5, 6]},
                     {'id': 5, 'name': 'mohammadreza', 'friends': [3, 4, 6]},
                     {'id': 6, 'name': 'aria', 'friends': [4, 5]},
                     {'id': 7, 'name': 'firooz', 'friends': [3, 8, 9]},
                     {'id': 8, 'name': 'denis', 'friends': [7, 9]},
                     {'id': 9, 'name': 'jack', 'friends': [8, 7]}]

