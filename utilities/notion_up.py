from notion.client import NotionClient
from notion.block import PageBlock, TextBlock
from md2notion.upload import upload
from md2notion.NotionPyRenderer import addLatexExtension, NotionPyRenderer
import sys
import os
from datetime import datetime

def no_upload(filename):
    # Slice the source file
    with open(filename, 'r', encoding='utf-8') as source:
        content = source.read()

    # try:
    #     print('Slicing source file at {} \n'.format(content.index(marker)))
    #     uptext = content.split(marker)

    #     if len(uptext) == 2:
    #         uptext = uptext[1]
    #     else:
    #         raise Exception('Multiple markers detected!')
    # except:
    #     answer = input('No slicing marker found in {}. Continue to upload the whole doc? (Y/n) \n'.format(os.path.basename(filename))) or 'Y'

    #     if answer == 'Y' or answer == 'y':
    #         uptext = content
    #     elif answer == 'N' or answer == 'n':
    #         pass
    #     else:
    #         raise Exception('Please provide a valid input!')

    with open('upload_temp.md', 'w', encoding='utf-8') as f:
        f.write(content)

    with open('upload_temp.md', 'r', encoding='utf-8') as mdFile:
        text = page.children.add_new(PageBlock, title=os.path.basename(filename)+current_time)
        upload(mdFile, text, notionPyRendererCls=addLatexExtension(NotionPyRenderer))

    os.remove('upload_temp.md') # remove temporary file


now = datetime.now()
current_time = ' - ' + now.strftime("%H:%M:%S")

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="v02%3Auser_token_or_cookies%3AKTo8lEF74O-Tb6e2Q8Lze5Sg4sl4FPtHT6yr5jOt1EXivfdsls3Yw8rZOaapSGhyQMX8fDs_sJmPQCQVk-aVSd7i0P-er3YS8n64WONqMtBNwVXQ3pXDOfP1EacZWYNQBu3h")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/Upload-461ba63643244e8f968eb3a11ca7a2a9")

# Marker for content that needs to be uploaded. It looks like:
'''
---

Upload starts here!

---
'''
marker = 'Upload starts here!\n\n---\n\n'

path_list = []

# File directory
if len(sys.argv) >= 2:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            path_list.append(arg)
        if os.path.isdir(arg):
            for root, dirs, files in os.walk(arg):
                for file in files:
                        path_list.append(os.path.join(root, file))
        else:
            pass
else:
    while True:
        filepath = str(input('Key in the path of a source file or directory: (empty input to continue)'))
        if os.path.isfile(filepath):
            path_list.append(filepath)
        elif os.path.isdir(filepath):
            for root, dirs, files in os.walk(filepath):
                for file in files:
                        path_list.append(os.path.join(root, file))
        else:
            break

assert path_list # check that path_list is non-empty

print('Uploading following files:')
for filepath in path_list:
    print(os.path.basename(filepath))
print("Modifying page titled: {} \n".format(page.title))

answer = input('Continue? (Y/n) \n') or 'Y'

if answer == 'Y' or answer == 'y':
    pass
elif answer == 'N' or answer == 'n':
    raise SystemExit('Aborting upload!')
else:
    raise Exception('Please provide a valid input!')

for filepath in path_list:
    no_upload(filepath)


print('\n---UPLOAD COMPLETE---')