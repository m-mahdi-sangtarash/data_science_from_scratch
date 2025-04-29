# import pandas as pd
# import numpy as np
#
# dataset = pd.read_csv("users_dataset.csv")
#
# users_data = {}
# for index, row in dataset.iterrows():
#     user_friends_list = []
#     user_friends = row['friends'].split(",")
#     for user_friend in user_friends:
#         user_friends_list.append(int(user_friend))
#     user_data = {"id": index,
#                  "name": row['user_name'],
#                  "friends": user_friends_list}
#     print(user_data)


def find_best_suggestion(users_dataset: list, user_id: int):
    """

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

