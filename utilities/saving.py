import os
import sys
import time

path_list = []


def cleanup(filename, output_path):
    '''
    Cleans up the output file.
    '''
    if output_path.endswith('.md'):
        if filename.endswith('.ipynb'):
            with open(output_path, 'r', encoding='utf-8') as source:
                lines = source.readlines()
            with open(output_path, 'w', encoding='utf-8') as source:
                for line in lines:
                    if ':::' not in line:
                        source.write(line)
                    else:
                        pass
    else:
        pass


def pan_save(filepath, fontsize=14, linespacing=1.0, options=[]):
    '''
    Save a file using pandoc
    '''
    filename = os.path.basename(filepath)

    # check if saved folder exists
    if not os.path.exists('saved'):
        os.makedirs('saved')

    output_path = 'saved\\' + filename[:  filename.find('.')] + '.' + format_ext

    # check if options is empty
    if options != ['']:
        opt_sting = ''
        for option in options:
            opt_sting += '-V ' + option + ' '
    else:
        opt_sting = ''

    command = 'pandoc {} -V geometry:margin=1in -V fontsize={} -V linestretch={} -o {} --wrap=preserve {}'.format(filepath, fontsize, linespacing, output_path, opt_sting)

    print('Saving {} as a .{} file...'.format(filename,  format_ext))
    os.system(command)

    cleanup(filename, output_path)


if len(sys.argv) >= 2:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            path_list.append(arg)
        if os.path.isdir(arg):
            for root, dirs, files in os.walk(arg):
                for file in files:
                        path_list.append(os.path.join(root, file))
else:
    while True:
        filepath = str(input('Key in the path of a source file or directory: (empty input to continue)'))
        if os.path.isfile(filepath):
            path_list.append(filepath)
        if os.path.isdir(filepath):
            for root, dirs, files in os.walk(filepath):
                for file in files:
                        path_list.append(os.path.join(root, file))
        else:
            break

assert path_list # check that path_list is non-empty

fontsize = int(input('Key in the desired fontsize (default 14):') or '14')

linespacing = float(input('Key in the desired line spacing (default 1.5):') or '1.5')

# Ask for other arguments passed as kwargs as a string separated by comma
other_args = str(input('Key in other arguments separated by comma:') or '').split(',')

format_ext = str(input('Key in the desired file extension (default pdf):') or 'pdf')

print('Saving following files:')
for filepath in path_list:
    print(os.path.basename(filepath))

print('\nFont size: {} \nLine spacing: {} \nFormat: {}'.format(fontsize, linespacing, format_ext))

answer = input('\nContinue? (Y/n)') or 'Y'

if answer == 'Y' or answer == 'y':
    pass
elif answer == 'N' or answer == 'n':
    raise SystemExit('Aborting upload!')
else:
    raise Exception('Please provide a valid input!')

for filepath in path_list:
    pan_save(filepath, fontsize=fontsize, linespacing=linespacing, options=other_args)
    
print('---SAVING COMPLETE---')