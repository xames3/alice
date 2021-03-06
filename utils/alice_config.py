# Copyright 2019 XA. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
# =============================================================================
#
#                           A . L . I . C . E
#                A Logically Interacting Computing Entity
#
# =============================================================================

"""
ALICE CONFIG
=============

Alice Config is used for accessing the named variables and necessary functions
for operational sharing.

## Basic usage as a module:

    import alice_config as alice

Read comments before you try modifying this file.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from datetime import datetime, date
import os
import random
import socket
import requests

try:
    from urllib2 import urlopen, URLError
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
    from urllib.request import urlopen, URLError


class NetworkStatus(object):
    """
    Checks if the system is connected to the network or note.
    """
    google_url = 'https://www.google.com/'

    def __init__(self):
        pass

    def test_internet(self):
        try:
            data = urlopen(self.google_url, timeout=5)
        except URLError:
            return False, random.choice(['# No network detected.', '# I\'m offline.', '# We\'re offline.'])

        try:
            host = data.fp._sock.fp._sock.getpeername()
        except AttributeError:
            host = data.fp.raw._sock.getpeername()

        self.google_url = 'http://' + (host[0] if len(host) == 2 else
                                       socket.gethostbyname(urlparse(data.geturl()).hostname))

        return True, random.choice(['# I\'m online and ready.', '# I\'m online.', '# We\'re online.'])


def create_dir(dir_name):
    """
    Creates a new folder in case folder does not exists.

    If the folder is already present it'll ignore the function and move on to
    the next line.

    Arguments:
        dir_name: Folder to be created.

    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def convert_bytes(size_in_bytes):
    """
    Converts bytes to MB, GB, etc.

    Arguments:
        size_in_bytes: Actual size of a file/folder in bytes.

    """
    # Iterate through the file size suffixes
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return '%3.1f %s' % (size_in_bytes, x)
        size_in_bytes /= 1024.0


def file_size(file_path):
    """
    Returns the file size.

    Arguments:
        file_path: Path to the file whose file size needs to be calculated.

    """
    if os.path.isfile(file_path):
        file_size_info = os.stat(file_path)
        return convert_bytes(file_size_info.st_size)


def location_details(location):
    checker = NetworkStatus()
    net_stat, alice_stat = checker.test_internet()
    if net_stat is True:
        locate_url = 'https://api.ipdata.co?api-key=test'
        dispostion = requests.get(locate_url).json()
        return dispostion[location]
    else:
        return alice_stat


# Self dispostion
print_alice = 'A . L . I . C . E '
shortname = 'Alice'
fullname = 'A Logically Interacting Computing Entity'
codename = 'cassiopeia'
current_version = '1.2.4.20190406'
gender = random.choice(['Woman', 'Girl', 'Female', 'Lady'])
created_date = birthday = date(2018, 11, 27)
today_date = date.today()
date_difference = today_date - created_date
current_age = date_difference.days
primary_language = 'English'
language_code = 'EN'

# XA's details
creator_name = random.choice(['XA', 'Mr. XA', 'Boss'])
creator_gender = random.choice(['Guy', 'Man', 'Gentleman'])
creator_next_birthday = date(int((date.today().year) + 1), 5, 4)

# Welcome greetings
current_hour = datetime.now().hour
wish_time = 'Night' if current_hour > 21 and current_hour < 4 else \
            'Good morning' if 5 <= current_hour < 12 else \
            'Good afternoon' if current_hour < 18 else \
            'Good evening'
timezone = 'night' if current_hour > 21 and current_hour < 4 else \
    'morning' if 5 <= current_hour < 12 else \
    'afternoon' if current_hour < 18 else \
    'evening'
greetings = random.choice(['lovely', 'wonderful', 'beautiful', 'great'])

# Root directory structure (Do not change)
current_file = os.path.abspath(__file__)
utils_dir = os.path.dirname(current_file)
package_dir = os.path.dirname(utils_dir)
engine_dir = os.path.join(package_dir, 'engine\\')
core_dir = os.path.join(engine_dir, 'core\\')
files_dir = os.path.join(engine_dir, 'files\\')
json_dir = os.path.join(engine_dir, 'json\\')
legacy_dir = os.path.join(engine_dir, 'legacy\\')
layers_dir = os.path.join(engine_dir, 'layers\\')
logs_dir = os.path.join(engine_dir, 'logs\\')
model_dir = os.path.join(engine_dir, 'model\\')
assistance_dir = os.path.join(core_dir, 'assistance\\')
character_dir = os.path.join(core_dir, 'character\\')
datasets_dir = os.path.join(core_dir, 'datasets\\')
parsed_dir = os.path.join(datasets_dir, 'parsed\\')

# Json files (Do not change)
hparams_file = os.path.join(json_dir, 'hparams.json')
pparams_file = os.path.join(json_dir, 'pparams.json')

# Xames3 files (Do not change)
vocab_file = os.path.join(core_dir, 'vocab.xames3')
assistant_file = os.path.join(assistance_dir, 'assistant.xames3')
arithmetics_file = os.path.join(assistance_dir, 'arithmetics.xames3')
datetime_file = os.path.join(assistance_dir, 'datetime.xames3')
name_file = os.path.join(character_dir, 'name.xames3')
personality_file = os.path.join(character_dir, 'personality.xames3')
unk_file = os.path.join(character_dir, 'unk.xames3')
subreddits_file = os.path.join(legacy_dir, 'subreddits.xames3')
exception_file = os.path.join(legacy_dir, 'exception.xames3')
cassiopeia_file = os.path.join(parsed_dir, 'cassiopeia.xames3')
cassiopeia_temp_file = os.path.join(parsed_dir, 'cassiopeia_temp.xames3')
cassiopeia_cleaned_file = os.path.join(parsed_dir, 'cassiopeia_cleaned.xames3')
dict_file = os.path.join(layers_dir, 'dict.xames3')
stories_file = os.path.join(layers_dir, 'stories.xames3')
jokes_file = os.path.join(layers_dir, 'jokes.xames3')

# Bz2 file (Do not change)
cassiopeia_output_file = os.path.join(parsed_dir, 'cassiopeia.bz2')

# Extensions
py_file = '.py'
pdf_file = '.pdf'
png_file = '.png'
gif_file = '.gif'
bmp_file = '.bmp'
bz2_file = '.bz2'
zip_file = '.zip'
mp3_file = '.mp3'
mp4_file = '.mp4'
avi_file = '.avi'
txt_file = '.txt'
exe_file = '.exe'
msi_file = '.msi'
xml_file = '.xml'
apk_file = '.apk'
jpeg_file = '.jpeg'
json_file = '.json'
html_file = '.html'
xames3_file = '.xames3'

# Comment and conversation line seperator
comment_line_sep = '=='
conversation_sep = '==='

# Length variables
max_len = 1000
hparams_len = 50
