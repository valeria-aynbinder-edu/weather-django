import argparse


def remove_stutters(input_file, output_file):
    print(f"received minput dfile: {input_file}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remove stutters from text')
    parser.add_argument('input_file', type=str,  help='input file path')
    parser.add_argument('output_file',type=str,  help='input file path')
    parser.add_argument('--num',  type=int, help='just a num')

    args = parser.parse_args()
    # print(args.accumulate(args.integers))


    remove_stutters(args.input_file, args.output_file)