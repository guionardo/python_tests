import getopt
import glob
import io
import os
import sys

from progress.spinner import PixelSpinner
from tqdm import tqdm
from image_mover import ImageMover

options = [
    ('h', 'help', 'Show usage options'),
    ('i:', 'inputfolder', 'Folder with source images'),
    ('o:', 'outputfolder', 'Folder where images are copied/moved'),
    ('r:', 'recursive', 'Recursive search'),
    ('f:', 'folderpattern', 'Folder pattern: default = yyyy/mm'),
    ('c', 'nomove', 'No move, just copy files')
]

version = "0.1"


def usage(message=None):
    print(f"\nImage Organizer {version}")
    print("Options:")
    w = [0, 0]
    for option in options:
        w[0] = w[0] if len(option[1]) < w[0] else len(option[1])
        w[1] = w[1] if len(option[2]) < w[1] else len(option[2])
    for option in options:
        print("   -{:<2} | --{:<{w0}}  {:<{w1}}".format(
            option[0], option[1], option[2], w0=w[0], w1=w[1]))

    if message is not None:
        print('\nERRORS:\n')
        message = [message] if isinstance(message, str) else message
        for msg in message:
            print("  ", msg)

    print()


def get_sources(inputFolder, recursive):
    extensions = ['jpg', 'jpeg', 'gif', 'png']
    sources = []
    paths = []
    try:
        with PixelSpinner(f'Reading file names from {inputFolder} ') as bar:
            for f in glob.iglob(os.path.join(inputFolder, '*.*'), recursive=recursive):
                bar.next()
                for ext in extensions:
                    if f.lower().endswith(ext):
                        im = ImageMover(f)
                        sources.append(im)
                        if os.path.dirname(f) not in paths:
                            paths.append(os.path.dirname(f))
                        break
        print(f"Found {len(sources)} files in {len(paths)} folders\n")

    except Exception as e:
        return str(e)

    return sources


def get_parsed(sources):
    try:
        print(f'Parsing {len(sources)} files...')
        for i in tqdm(range(len(sources))):
            sources[i].parse()
        print(f'Parsing done')
    except Exception as e:
        return str(e)

    return sources


def do_process(parsed, outputfolder, folderpattern, nomove):
    try:
        print(f"Processing {len(parsed)} files")
        for i in tqdm(range(len(parsed))):
            parsed[i].transfer(outputfolder, folderpattern, nomove)
        print('Processing done')
        return True
    except Exception as e:
        return str(e)


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "hi:o:", ["inputfolder=", "outputfolder="])
    except getopt.GetoptError as e:
        print(__file__, "test.py -i <inputfile> -o <outputfile>: ", str(e))
        sys.exit(2)

    inputFolder = ""
    outputFolder = ""
    recursive = False
    folderpattern = "%Y/%m"
    nomove = False

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--inputfolder"):
            inputFolder = arg
        elif opt in ("-o", "--outputfolder"):
            outputFolder = arg
        elif opt in ('-r', '--recursive'):
            recursive = True
        elif opt in ('-f', '--folderpattern'):
            folderpattern = arg
        elif opt in ('-c', '--nomove'):
            nomove = True

    errors = []

    if not inputFolder:
        errors.append('Input folder is missing')
    elif not os.path.isdir(inputFolder):
        errors.append(f'Input folder {inputFolder} not found')

    if not outputFolder:
        errors.append('Output folder is missing')
    else:
        try:
            outputFolder = os.path.realpath(outputFolder)
            testOutput = os.path.join(outputFolder, '.image_organizer.test')
            with open(testOutput, 'w') as f:
                f.write('Test')
                f.close()
            os.unlink(testOutput)
        except Exception as e:
            errors.append(
                f'Output folder {outputFolder} writing error: {str(e)}')

    if len(errors):
        usage(errors)
        return

    sources = get_sources(inputFolder, recursive)
    if isinstance(sources, str):
        usage(sources)
        return

    parsed = get_parsed(sources)
    if isinstance(parsed, str):
        usage(parsed)
        return

    process = do_process(parsed, outputFolder, folderpattern, nomove)


if __name__ == "__main__":
    main(sys.argv[1:])
