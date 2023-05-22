import argparse
from .wrapper import create


def main():
    parser = argparse.ArgumentParser(
        description="A simple cosmic ray generator"
    )
    parser.add_argument(
        "n", type=int,
        help="The number of muons to be generated",
        default=1
    )
    parser.add_argument(
        "--llim", "-l",
        help=("Lower energy limit for muons"),
        default=0
    )
    parser.add_argument(
        "--ulim", "-u",
        help=("Upper energy limit for muons"),
        default=500
    )
    parser.add_argument(
        "--with-times",
        help=("Sets the generator to not assign timestamps to muon"),
        action='store_true', dest='times'
    )
    parser.add_argument(
        "--no-angles",
        help=("Sets the generator to not assign angles to muon"),
        action='store_false', dest='angles'
    )
    parser.add_argument(
        "--det", "-d",
        type=float,
        help=("Used to specify detector area. Required if times is set to True."),
        default=None
    )
    parser.set_defaults(times=False, angles=True)
    args = parser.parse_args()
    sol=create(n=args.n, llim=args.llim, ulim=args.ulim, times=args.times, with_angles=args.angles, detector_area=args.det)
    for i in sol:
        print(i)

if __name__ == "__main__":
    main()