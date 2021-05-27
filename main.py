import os
import random

from skpy import Skype, SkypeConnection


def get_random_image(path):
    return '{0}/{1}'.format(path, random.choice(os.listdir(path)))


if __name__ == '__main__':
    # API endpoint to change avatar
    API_AVATAR = 'https://avatar.skype.com'
    USER = os.getenv('SKYPE_USER')
    CREDENTIAL = os.getenv('CREDENTIAL')
    IMAGES_PATH = os.getenv('IMAGES_PATH')

    # Create new Skype instance
    sk = Skype(USER, CREDENTIAL)

    content_header = {'Content-type': 'image/jpeg'}

    print('¯\_(ツ)_/¯ Randomly pick a meme to update avatar')
    try:
        new_img = get_random_image(IMAGES_PATH)
        print('New image: ' + new_img)
        with open(new_img, 'rb') as f:
            sk.conn('PUT', "{0}/v1/avatars/{1}".format(API_AVATAR, sk.userId),
                    auth=SkypeConnection.Auth.SkypeToken, data=f.read(), headers=content_header)
        print('Uploaded avatar successfully')
    except Exception as e:
        print('¯\_(ツ)_/¯ Failed to update new avatar as', e)
