import argparse


def lev_dist(text_1, text_2):
    len1 = len(text_1)
    len2 = len(text_2)

    if len1 < len2:
        text_1, text_2 = text_2, text_1
        len1, len2 = len2, len1

    m = [[i for i in range(len2 + 1)], [0] * (len2 + 1)]
    m[1][0] += 1

    for i in range(len1):
        for j in range(len2):
            m[1][j + 1] = min([m[1][j] + 1, m[0][j + 1] + 1,
                              m[0][j] + (1 if text_1[i] != text_2[j] else 0)])

        m = [m[1], [0] * len(m[1])]
        m[1][0] += i + 3

    return m[0][-1]


def _score(f1_path, f2_path):

    with open(f1_path, 'r') as f:
        text_1 = f.read()

    with open(f2_path, 'r') as f:
        text_2 = f.read()

    ld = lev_dist(text_1, text_2)
    score = (len(text_1) - ld) / len(text_2)
    return score


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    args = parser.parse_args()

    with open(args.input, 'r') as input_file:
        for l in input_file.readlines():
            text_1, text_2 = l.split()
            score = _score(text_1, text_2)
            with open(args.output, 'a+') as output_file:
                output_file.write(str(score) + '\n')
